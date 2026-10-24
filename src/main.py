from pathlib import Path

# Busca datos/productos.txt a partir de donde está este archivo,
# así funciona desde cualquier carpeta (terminal o botón ▶ de VS Code)
carpeta_proyecto = Path(__file__).parent.parent
archivo = carpeta_proyecto / "datos" / "productos.txt"

lineas = archivo.read_text(encoding="utf-8").splitlines()

print("=== Inventario Tienda Don Pedro ===")

total_productos = 0
valor_inventario = 0

for linea in lineas[2:]:
    print("-", linea)
    total_productos += 1
    # Toma lo que está después del "$" y quita el punto de miles
    precio = linea.split("$")[1].replace(".", "")
    valor_inventario += int(precio)

print("Total de productos:", total_productos)
print("Valor del inventario: $" + str(valor_inventario))