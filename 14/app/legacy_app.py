from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Callable
from app.core.taxes import calculate_tax_logic

app = FastAPI()

class OrderItem(BaseModel):
    product_id: int
    quantity: int
    price: float

# --- O Segredo da Refatoração ---
# Criamos uma função que "entrega" a lógica de cálculo.
# Isso permite que o FastAPI injete essa dependência, 
# e que nós a substituamos nos testes.
def get_tax_calculator() -> Callable[[float], float]:
    return calculate_tax_logic

@app.post("/orders/")
def create_order(
    item: OrderItem, 
    # Aqui usamos a Injeção de Dependência
    tax_calculator: Callable = Depends(get_tax_calculator)
):
    if item.quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantidade inválida")

    total = item.price * item.quantity
    
    # A rota não sabe COMO calcular, ela apenas pede para a calculadora
    tax = tax_calculator(total)
    
    final_price = total + tax

    # (Simulação de salvar no banco de dados omitida para focar na lógica)
    
    return {
        "product_id": item.product_id, 
        "final_price": final_price, 
        "tax": tax
    }