import sys

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):

    # Načte prvních `header_length` bytů ze souboru `file_name` a vrátí je jako binární řetězec.

    with open(file_name, 'rb') as f:
        header = f.read(header_length) #cteni headru ze souboru
    return header


def is_jpeg(file_name):

    #Zkontroluje, zda soubor začíná hlavičkou JPEG.

    header = read_header(file_name, len(jpeg_header))
    return header == jpeg_header


def is_gif(file_name):

    #Zkontroluje, zda soubor začíná hlavičkou GIF87a nebo GIF89a.

    header = read_header(file_name, max(len(gif_header1), len(gif_header2)))
    return header == gif_header1 or header == gif_header2


def is_png(file_name):

    #Zkontroluje, zda soubor začíná hlavičkou PNG.

    header = read_header(file_name, len(png_header))
    return header == png_header


def print_file_type(file_name):

    #Vypíše typ souboru (funkci neupravujte).

    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')


if __name__ == '__main__':
    try:
        file_name = sys.argv[1] # první argumetn z přikaz radky
        print_file_type(file_name)
    except IndexError:
        print("Chyba: Nebyl zadán název souboru.\nPoužití: python fifth.py cesta/k/obrazku.jpg")
    except Exception as e:
        print(f"Nastala chyba: {e}")

#pro spuštění se musí spustit příkazová řádka a do ní zapsat: fifth.py (název_souboru)
