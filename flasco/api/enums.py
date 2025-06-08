from fastapi import APIRouter
from flasco.application.enums.curso import Curso
from flasco.application.enums.formacao import Formacao

router = APIRouter(prefix="/enums",tags=["Enums"])

@router.get("/curso")
def listar_cursos():
    print(list(Curso))
    return [
        {
            "name": c.name,
            "value": c.value,
            "label": c.value.replace("_", " ").title()
        }
        for c in Curso
    ]

@router.get("/formacao")
def listar_formacao():
    return [
        {
            "name": f.name,
            "value": f.value,
            "label": f.value.replace("_", " ").title()
        }
        for f in Formacao
    ]