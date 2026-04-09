from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from app.config import DATABASE_URL

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    from app.models import customer, employee, integrations, report, user, billing, medical_exam, epi_purchase
    from app.models.billing import PayrollItemType, PayrollDirection
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        from app.models.user import User
        admin_email = "ti@grupoopus.com"
        existing_admin = db.query(User).filter(User.email == admin_email).first()
        if not existing_admin:
            admin = User(
                username=admin_email,
                email=admin_email,
                full_name="Administrador",
                is_active=1
            )
            admin.set_password("telos@2026")
            db.add(admin)
            db.commit()

        existing = db.query(PayrollItemType).first()
        if not existing:
            default_types = [
                PayrollItemType(code="SALARIO_DIA", description="Salário Dia", group="REMUNERACAO", direction=PayrollDirection.CREDIT),
                PayrollItemType(code="HORA_EXTRA", description="Horas Extras", group="REMUNERACAO", direction=PayrollDirection.CREDIT),
                PayrollItemType(code="VALE_TRANSPORTE", description="Vale Transporte", group="BENEFICIOS", direction=PayrollDirection.DEBIT),
                PayrollItemType(code="VALE_REFEICAO", description="Vale Refeição", group="BENEFICIOS", direction=PayrollDirection.DEBIT),
                PayrollItemType(code="PREMIO_BONUS", description="Prêmio/Bônus", group="REMUNERACAO", direction=PayrollDirection.CREDIT),
                PayrollItemType(code="TRIBUTO_VALOR", description="Tributos", group="ENCARGOS", direction=PayrollDirection.DEBIT),
                PayrollItemType(code="ENCARGO_VALOR", description="Encargos", group="ENCARGOS", direction=PayrollDirection.DEBIT),
                PayrollItemType(code="TAXA_FATURAMENTO", description="Taxa de Faturamento", group="TAXAS", direction=PayrollDirection.DEBIT),
                PayrollItemType(code="EXAME_MEDICO", description="Exame Médico", group="SAUDE", direction=PayrollDirection.DEBIT),
            ]
            db.add_all(default_types)
            db.commit()
    finally:
        db.close()
