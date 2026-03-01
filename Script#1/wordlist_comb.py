import argparse

def combinar_wordlists(archivo_usuarios, archivo_contrasenas, archivo_salida):
    try:
        with open(archivo_usuarios, 'r', encoding='utf-8') as f_users, \
             open(archivo_contrasenas, 'r', encoding='utf-8') as f_passwords, \
             open(archivo_salida, 'w', encoding='utf-8') as f_out:
            
            contrasenas = f_passwords.readlines()
            
            for usuario in f_users:
                usuario_limpio = usuario.strip()
                for contrasena in contrasenas:
                    contrasena_limpia = contrasena.strip()
                    
                    if usuario_limpio and contrasena_limpia:
                        f_out.write(f"{usuario_limpio}:{contrasena_limpia}\n")
                        
        print(f"[+] ¡Éxito! Wordlist combinada guardada en: {archivo_salida}")
        
    except FileNotFoundError as e:
        print(f"[-] Error: No se pudo encontrar uno de los archivos. Detalles: {e}")
    except Exception as e:
        print(f"[-] Ocurrió un error inesperado: {e}")

if __name__ == '__main__':
    # Configuración de los argumentos de la línea de comandos
    parser = argparse.ArgumentParser(description="Combina una lista de usuarios y contraseñas en formato usuario:contraseña")
    
    parser.add_argument("-u", "--usuarios", required=True, help="Ruta al archivo de texto con los usuarios")
    parser.add_argument("-p", "--contrasenas", required=True, help="Ruta al archivo de texto con las contraseñas")
    parser.add_argument("-o", "--salida", default="resultado.txt", help="Nombre del archivo de salida (por defecto: resultado.txt)")
    
    args = parser.parse_args()
    
    # Ejecutamos la función con los argumentos pasados por el usuario
    combinar_wordlists(args.usuarios, args.contrasenas, args.salida)