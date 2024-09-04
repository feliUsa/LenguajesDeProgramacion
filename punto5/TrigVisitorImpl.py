import math
from TrigParser import TrigParser
from TrigVisitor import TrigVisitor

class TrigVisitorImpl(TrigVisitor):

    def visitExpr(self, ctx: TrigParser.ExprContext):
        func_name = ctx.trigFunc().getText()
        value = float(ctx.NUMBER().getText())
        value = math.radians(value)  # Convertir a radianes

        if func_name == "Sin":
            return math.sin(value)
        elif func_name == "Cos":
            return math.cos(value)
        elif func_name == "Tan":
            return math.tan(value)
        else:
            raise ValueError(f"Función desconocida: {func_name}")
