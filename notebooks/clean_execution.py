#!/usr/bin/env python3
import argparse
import nbformat
import sys
import os
from pathlib import Path
import tempfile
import shutil

# --- CONFIGURACIÓN DE IMPRESIÓN ---
# Forzamos que los prints salgan inmediatamente (sin buffer)
def log(msg):
    print(msg, flush=True)

def clean_notebook(nb_path: Path):
    log(f"   📂 Procesando archivo: {nb_path.name}...")
    
    try:
        # 1. Leer
        nb = nbformat.read(nb_path, as_version=4)
        
        # 2. Definir claves a borrar
        keys_to_clean_cell = ['collapsed', 'scrolled'] 
        keys_to_clean_nb = ['dirty', 'widgets']
        
        cleaned_cells = 0

        # 3. Limpiar Notebook Metadata
        if 'metadata' in nb:
            for key in keys_to_clean_nb:
                if key in nb.metadata:
                    del nb.metadata[key]

        # 4. Iterar celdas
        for i, cell in enumerate(nb.cells):
            # Limpiar contadores (Code)
            if cell.cell_type == 'code':
                if cell.execution_count is not None:
                    cell.execution_count = None
                    cleaned_cells += 1
                
                for output in cell.get('outputs', []):
                    if 'execution_count' in output:
                        output.execution_count = None

            # Limpiar visibilidad (Code y Markdown)
            # Borrar collapsed/scrolled de la raíz
            for key in keys_to_clean_cell:
                if key in cell.metadata:
                    log(f"      - Celda {i}: Eliminado '{key}'")
                    del cell.metadata[key]
            
            # Borrar jupyter.outputs_hidden
            if 'jupyter' in cell.metadata:
                if 'outputs_hidden' in cell.metadata['jupyter']:
                    log(f"      - Celda {i}: Eliminado 'jupyter.outputs_hidden'")
                    del cell.metadata['jupyter']['outputs_hidden']
                if 'source_hidden' in cell.metadata['jupyter']:
                    del cell.metadata['jupyter']['source_hidden']
                if not cell.metadata['jupyter']:
                    del cell.metadata['jupyter']

        # 5. Escritura Atómica
        log(f"   💾 Guardando cambios en {nb_path.name}...")
        with tempfile.NamedTemporaryFile(mode='w', dir=nb_path.parent, delete=False, encoding='utf-8') as tmp_file:
            nbformat.write(nb, tmp_file)
            tmp_path = Path(tmp_file.name)
        
        shutil.move(tmp_path, nb_path)
        log(f"   ✅ ÉXITO: {nb_path.name} guardado. ({cleaned_cells} celdas limpiadas).\n")

    except Exception as e:
        log(f"   ❌ ERROR CRÍTICO en {nb_path.name}: {e}")
        import traceback
        traceback.print_exc()
        if 'tmp_path' in locals() and tmp_path.exists():
            os.remove(tmp_path)

if __name__ == "__main__":
    log("--- INICIO DEL SCRIPT ---")
    
    parser = argparse.ArgumentParser(description="Limpia notebooks.")
    # 'nargs' asegura que capture todos los argumentos pasados
    parser.add_argument('notebooks', metavar='N', type=str, nargs='+', help='Rutas de los archivos .ipynb')
    
    # Si no se pasan argumentos, argparse mostrará error automáticamente y saldrá.
    # Pero si estás en un entorno raro, capturamos el intento:
    if len(sys.argv) == 1:
        log("❌ ERROR: No pasaste ningún archivo como argumento.")
        log("   Uso correcto: python clean.py tu_archivo.ipynb")
        sys.exit(1)

    args = parser.parse_args()
    
    log(f"📋 Archivos recibidos: {args.notebooks}")

    for path_str in args.notebooks:
        # Convertir a Path y resolver ruta absoluta para evitar dudas
        path = Path(path_str).resolve()
        
        if not path.exists():
            log(f"⚠️  AVISO: El archivo no existe en la ruta: {path}")
            continue
            
        if path.suffix != '.ipynb':
            log(f"⚠️  AVISO: El archivo no termina en .ipynb: {path}")
            continue

        clean_notebook(path)
        
    log("--- FIN DEL SCRIPT ---")
