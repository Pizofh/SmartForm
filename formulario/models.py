
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Recluta(models.Model):

    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30, blank=True)
    primer_apellido = models.CharField(max_length=80)
    segundo_apellido = models.CharField(max_length=80, blank=True)
    
    tipo_documento = models.CharField("Tipo de documento", max_length=2, choices=[
        ("CC", "Cédula Ciudadanía"),
        ("CE", "Cédula Extranjería"),
    ])
    numero_documento = models.IntegerField("Número de documento", unique=True,validators=[MinValueValidator(1_000), MaxValueValidator(99_999_999_999)])
    fecha_expedición = models.DateField("Fecha de expedición de la cédula")
    lugar_expedición = models.CharField("Lugar de expedición", max_length=20)
    pasaporte_numero = models.CharField("Pasaporte No", max_length=12, blank=True)
    fecha_pasaporte = models.DateField("Fecha de expedición del pasaporte", null=True, blank=True)
    numero_libretamilitar = models.IntegerField("Libreta militar No", null=True, blank=True,validators=[MinValueValidator(1_000), MaxValueValidator(99_999_999_999)])
    clase_libretamilitar = models.CharField("Clase de Libreta militar", max_length=10, null=True, choices=[
        ("1C", "Primera Clase"), ("2C", "Segunda Clase"), ("Pv", "Provisional"),
        ("Ex", "Exonerado"), ("Sr", "Sin Resolver"), ("N/A", "No Aplica"),
    ])
    distrito_militar = models.CharField("Distrito Militar", max_length=50, blank=True)
    sobrenombres = models.CharField("Sobrenombres", max_length=30, blank=True)
    class Dia_Nacimiento(models.IntegerChoices):
        DIA_1 = 1, "1"
        DIA_31 = 31, "31"
    dia_nacimiento = models.IntegerField("Día de nacimiento", null=True, choices=[(i, str(i)) for i in range(1, 32)]) 
    mes_nacimiento = models.CharField("Mes de nacimiento", max_length=13, null=True, choices=[
        (str(i), mes) for i, mes in enumerate([
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ], start=1)
    ])
    año_nacimiento = models.IntegerField("Año de Nacimiento", null=True, validators=[
        MinValueValidator(1900), MaxValueValidator(2025)
    ])
    estado_civil = models.CharField("Estado Civil", max_length=30, null=True, choices=[
        ("Casado(a)", "Casado(a)"), ("Soltero(a)", "Soltero(a)"),
        ("Unión Marital de Hecho", "Unión Marital de Hecho"),
        ("Separado de Hecho", "Separado de Hecho"), ("Divorciado(a)", "Divorciado(a)"), ("Viudo(a)", "Viudo(a)"),
    ])
    profesion_oficio = models.CharField("Profesión u Oficio", max_length=30, null=True)
    tarjeta_profesional = models.CharField("Tarjeta profesional", max_length=15, null=True)
    señales_corporales = models.CharField("Señales corporales", max_length=50, null=True)
    estatura = models.IntegerField("Estatura (cm)", null=True, validators=[MinValueValidator(10), MaxValueValidator(400)])
    peso = models.IntegerField("Peso (kg)", null=True, validators=[MinValueValidator(30), MaxValueValidator(500)])
    tipo_via = models.CharField("Tipo de vía", max_length=20, null=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal = models.CharField("Número", max_length=10, null=True)
    letra_principal = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis = models.BooleanField("¿Bis?", default=False)
    letra_bis = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante = models.CharField("Cuadrante", max_length=10, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ], blank=True, null=True)
    numero_secundario = models.CharField("Número", max_length=10, null=True)
    letra_secundaria = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos = models.CharField("Cuadrante", max_length=10, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ], blank=True, null=True)
    nro = models.CharField("Número Final", max_length=30, blank=True, null=True)
    complemento = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True)
    barrio = models.CharField("Barrio", max_length=50,null=True)
    numero_celular = models.IntegerField("Número celular", unique=True,null=True,validators=[MinValueValidator(1_000), MaxValueValidator(99_999_999_999)])
    telefono_fijo = models.IntegerField("Numero de teléfono fijo", blank=True,null=True,validators=[MinValueValidator(1_000), MaxValueValidator(99_999_999_999)])
    ciudad = models.CharField("Ciudad de nacimiento", max_length=30,null=True)
    departamento = models.CharField("Departamento de nacimiento", max_length=30,null=True)
    correo_electronico_personal = models.EmailField("Correo Electrónico Personal",null=True)
    correo_electronico_institucional = models.EmailField("Correo Electrónico Institucional", blank=True,null=True)
    facebook = models.CharField("Cuenta de Facebook", max_length=50, blank=True,null=True)
    instagram =models.CharField("Cuenta de Instagram", max_length=50, blank=True,null=True)
    twitter = models.CharField("Cuenta de Twitter", max_length=50, blank=True,null=True)
    otras_redes = models.CharField("Otras Cuentas", max_length=50, blank=True,null=True)
    direccion_formateada = models.CharField(max_length=500, blank=True, null=True)


    class Meta:
     
        verbose_name = "Recluta"
        verbose_name_plural = "Reclutas"

    @property
    def nombres(self):
        return f"{self.primer_nombre} {self.segundo_nombre}".strip()

    @property
    def apellidos(self):
        return f"{self.primer_apellido} {self.segundo_apellido}".strip()

    @property
    def direccion_completa(self):
        partes = [
            self.tipo_via,
            self.numero_principal,
            self.letra_principal,
            "BIS" if self.bis else "",
            self.letra_bis,
            self.cuadrante,
        ]

        # solo incluye "#" si hay número_secundario
        if self.numero_secundario:
            partes.extend(["#", self.numero_secundario, self.letra_secundaria, self.cuadrante_dos])

        partes.append(self.nro)

        direccion = " ".join(filter(None, partes))
        if self.complemento:
            direccion += f", {self.complemento}"
        return direccion.strip()

    def save(self, *args, **kwargs):
        self.direccion_formateada = self.direccion_completa
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class DireccionesAnteriores(models.Model):

    recluta = models.ForeignKey('Recluta', on_delete=models.CASCADE, related_name='direcciones_anteriores',null=True)

    direccion_completa_anterior_1 = models.CharField(max_length=255, blank=True, null=True)
    direccion_completa_anterior_2 = models.CharField(max_length=255, blank=True, null=True)
    desde_1 = models.DateField("Desde",blank=True,null=True)
    hasta_1 = models.DateField("Hasta",blank=True,null=True)
    desde_2 = models.DateField("Desde",blank=True,null=True)
    hasta_2 = models.DateField("Hasta",blank=True,null=True)
    tipo_via_anterior_1 = models.CharField("Tipo de vía", max_length=20,blank=True, null=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_anterior_1 = models.CharField("Número", max_length=10, blank=True,null=True)
    letra_principal_anterior_1 = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_anterior_1 = models.BooleanField("¿Bis?", default=False)
    letra_bis_anterior_1 = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_anterior_1 = models.CharField("Cuadrante", max_length=10, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ], blank=True, null=True)
    numero_secundario_anterior_1 = models.CharField("Número", max_length=10,blank=True, null=True)
    letra_secundaria_anterior_1 = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_anterior_1 = models.CharField("Cuadrante", max_length=10, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ], blank=True, null=True)
    nro_anterior_1 = models.CharField("Número Final", max_length=30, blank=True, null=True)
    complemento_anterior_1 = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True)
    telefono_direccion_anterior_1_1 = models.IntegerField("Teléfono 1", blank=True,null=True,validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    telefono_direccion_anterior_1_2 = models.IntegerField("Teléfono 2", blank=True,null=True,validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    ciudad_direccion_anterior_1 = models.CharField("Ciudad", blank=True,null=True, max_length=25)



    tipo_via_anterior_2 = models.CharField("Tipo de vía", max_length=20,blank=True, null=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_anterior_2 = models.CharField("Número", max_length=10, blank=True,null=True)
    letra_principal_anterior_2 = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_anterior_2 = models.BooleanField("¿Bis?", default=False)
    letra_bis_anterior_2 = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_anterior_2 = models.CharField("Cuadrante", max_length=10, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ], blank=True, null=True)
    numero_secundario_anterior_2 = models.CharField("Número", max_length=10,blank=True, null=True)
    letra_secundaria_anterior_2 = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_anterior_2 = models.CharField("Cuadrante", max_length=10, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ], blank=True, null=True)
    nro_anterior_2 = models.CharField("Número Final", max_length=30, blank=True, null=True)
    complemento_anterior_2 = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True)
    telefono_direccion_anterior_2_1 = models.IntegerField("Teléfono 1", blank=True,null=True,validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    telefono_direccion_anterior_2_2 = models.IntegerField("Teléfono 2", blank=True,null=True,validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    ciudad_direccion_anterior_2 = models.CharField("Ciudad", blank=True,null=True, max_length=25)

    class Meta:
        verbose_name = "Dirección Anterior"
        verbose_name_plural = "Direcciones Anteriores"
    
    def __str__(self):
        return f"Direcciones Anteriores {self.id}"


class DatosFamiliares(models.Model):

    recluta = models.OneToOneField(Recluta, on_delete=models.CASCADE,null=True)

#DATOS CONYUGUE
    nombre_conyugue = models.CharField("Nombre del Cónyugue", max_length=50, blank=True)
    cedula_conyugue = models.CharField("Cédula del Cónyugue", max_length=15, blank=True, null=True)
    profesion_oficio_conyugue = models.CharField("Profesión del Cónyugue", max_length=50, blank=True, null=True)
    celular_conyugue = models.CharField("Celular del Cónyugue", max_length=15, blank=True)
    tipo_via_conyugue = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_conyugue = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_principal_conyugue = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_conyugue = models.BooleanField("¿Bis?", default=False)
    letra_bis_conyugue = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_conyugue = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_conyugue = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_secundaria_conyugue = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_conyugue = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_conyugue = models.CharField("Número Final", max_length=30, blank=True, null=True)
    complemento_conyugue = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True)
    direccion_formateada_conyugue = models.CharField(max_length=500, blank=True, null=True)

#DATOS PADRE
    nombre_padre = models.CharField("Nombre del padre", max_length=55,null=True)
    vive_padre = models.CharField("¿Vive?", null=True, choices=[("Sí", "Sí"), ("No","No")] )
    identificación_padre = models.IntegerField("CC No", null=True,validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    telefono_padre = models.IntegerField("Teléfono del Padre", blank=True, null=True,validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    oficio_profesion_padre = models.CharField("Profesión u Oficio", blank=True,null=True,max_length=50)
    tipo_via_padre = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_padre = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_principal_padre = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_padre = models.BooleanField("¿Bis?", default=False)
    letra_bis_padre = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_padre = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_padre = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_secundaria_padre = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_padre = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_padre = models.CharField("Número Final", max_length=30, blank=True, null=True)
    complemento_padre = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True)
    direccion_formateada_padre = models.CharField(max_length=500, blank=True, null=True)

#DATOS MADRE
    nombre_madre = models.CharField("Nombre del madre", max_length=55,null=True)
    vive_madre = models.CharField("¿Vive?", null=True, choices=[("Sí", "Sí"), ("No","No")] )
    identificación_madre = models.IntegerField("CC No", null=True,validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    telefono_madre = models.IntegerField("Teléfono de la Madre", blank=True, null=True,validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    oficio_profesion_madre = models.CharField("Profesión u Oficio de la Madre", blank=True,null=True,max_length=50)
    tipo_via_madre = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_madre = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_principal_madre = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_madre = models.BooleanField("¿Bis?", default=False)
    letra_bis_madre = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_madre = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_madre = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_secundaria_madre = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_madre = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_madre = models.CharField("Número Final", max_length=30, blank=True, null=True)
    complemento_madre = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True)
    direccion_formateada_madre = models.CharField(max_length=500, blank=True, null=True)

#DATOS HERMANO 1
    primer_apellido_hermano_1 = models.CharField("Primer Apellido", blank=True,null=True,max_length=30,)
    segundo_apellido_hermano_1 = models.CharField("Segundo Apellido", blank=True,null=True,max_length=30,)
    primer_nombre_hermano_1 = models.CharField("Primer Nombre", blank=True,null=True,max_length=30,)
    segundo_nombre_hermano_1 = models.CharField("Segundo Nombre", blank=True,null=True,max_length=30,)
    identificacion_hermano_1 = models.IntegerField("Identificación Hermano 1",blank=True, null=True, validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    ocupacion_hermano_1 = models.CharField("Ocupación Hermano 1",blank=True, null=True,max_length=60,)
    celular_hermano_1 = models.IntegerField("Celular Hermano 1", blank=True, null=True,validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    tipo_via_hermano_1 = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_hermano_1 = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_principal_hermano_1 = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_hermano_1 = models.BooleanField("¿Bis?", default=False)
    letra_bis_hermano_1 = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_hermano_1 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_hermano_1 = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_secundaria_hermano_1 = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_hermano_1 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_hermano_1 = models.CharField("Número Final", max_length=30, blank=True, null=True)
    complemento_hermano_1 = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True)
    direccion_formateada_hermano_1 = models.CharField(max_length=500, blank=True, null=True)


    #DATOS HERMANO 2
    primer_apellido_hermano_2 = models.CharField("Primer Apellido", blank=True,null=True,max_length=30,)
    segundo_apellido_hermano_2 = models.CharField("Segundo Apellido", blank=True,null=True,max_length=30,)
    primer_nombre_hermano_2 = models.CharField("Primer Nombre", blank=True,null=True,max_length=30,)
    segundo_nombre_hermano_2 = models.CharField("Segundo Apellido", blank=True,null=True,max_length=30,)
    identificacion_hermano_2 = models.IntegerField("Identificación Hermano 2",blank=True, null=True, validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    ocupacion_hermano_2 = models.CharField("Ocupación Hermano 2",blank=True, null=True,max_length=60,)
    celular_hermano_2 = models.IntegerField("Celular Hermano 2", blank=True, null=True,validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    tipo_via_hermano_2 = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_hermano_2 = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_principal_hermano_2 = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_hermano_2 = models.BooleanField("¿Bis?", default=False)
    letra_bis_hermano_2 = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_hermano_2 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_hermano_2 = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_secundaria_hermano_2 = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_hermano_2 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_hermano_2 = models.CharField("Número Final", max_length=30, blank=True, null=True)
    complemento_hermano_2 = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True)
    direccion_formateada_hermano_2 = models.CharField(max_length=500, blank=True, null=True)

#DATOS HERMANO 3

    primer_apellido_hermano_3 = models.CharField("Primer Apellido", blank=True,null=True,max_length=30,)
    segundo_apellido_hermano_3 = models.CharField("Segundo Apellido", blank=True,null=True,max_length=30,)
    primer_nombre_hermano_3 = models.CharField("Primer Nombre", blank=True,null=True,max_length=30,)
    segundo_nombre_hermano_3 = models.CharField("Segundo Nombre", blank=True,null=True,max_length=30,)
    identificacion_hermano_3 = models.IntegerField("Identificación Hermano 3",blank=True, null=True, validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    ocupacion_hermano_3 = models.CharField("Ocupación Hermano 3",blank=True, null=True,max_length=60,)
    celular_hermano_3 = models.IntegerField("Celular Hermano 3", blank=True, null=True,validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    tipo_via_hermano_3 = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_hermano_3 = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_principal_hermano_3 = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_hermano_3 = models.BooleanField("¿Bis?", default=False)
    letra_bis_hermano_3 = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_hermano_3 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_hermano_3 = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_secundaria_hermano_3 = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_hermano_3 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_hermano_3 = models.CharField("Número Final", max_length=30, blank=True, null=True)
    complemento_hermano_3 = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True)
    direccion_formateada_hermano_3 = models.CharField(max_length=500, blank=True, null=True)

#DATOS HERMANO 4

    primer_apellido_hermano_4 = models.CharField("Primer Apellido", blank=True,null=True,max_length=30,)
    segundo_apellido_hermano_4 = models.CharField("Segundo Apellido", blank=True,null=True,max_length=30,)
    primer_nombre_hermano_4 = models.CharField("Primer Nombre", blank=True,null=True,max_length=30,)
    segundo_nombre_hermano_4 = models.CharField("Segundo Nombre", blank=True,null=True,max_length=30,)
    identificacion_hermano_4 = models.IntegerField("Identificación Hermano 4",blank=True, null=True, validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    ocupacion_hermano_4 = models.CharField("Ocupación Hermano 4",blank=True, null=True,max_length=60,)
    celular_hermano_4 = models.IntegerField("Celular Hermano 4", blank=True, null=True,validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    tipo_via_hermano_4 = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_hermano_4 = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_principal_hermano_4 = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_hermano_4 = models.BooleanField("¿Bis?", default=False)
    letra_bis_hermano_4 = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_hermano_4 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_hermano_4 = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_secundaria_hermano_4 = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_hermano_4 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_hermano_4 = models.CharField("Número Final", max_length=30, blank=True, null=True)
    complemento_hermano_4 = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True)
    direccion_formateada_hermano_4 = models.CharField(max_length=500, blank=True, null=True)

#DATOS HERMANO 5

    primer_apellido_hermano_5 = models.CharField("Primer Apellido", blank=True,null=True,max_length=30,)
    segundo_apellido_hermano_5 = models.CharField("Segundo Apellido", blank=True,null=True,max_length=30,)
    primer_nombre_hermano_5 = models.CharField("Primer Nombre", blank=True,null=True,max_length=30,)
    segundo_nombre_hermano_5 = models.CharField("Segundo Nombre", blank=True,null=True,max_length=30,)
    identificacion_hermano_5 = models.IntegerField("Identificación Hermano 5",blank=True, null=True, validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    ocupacion_hermano_5 = models.CharField("Ocupación Hermano 5",blank=True, null=True,max_length=60,)
    celular_hermano_5 = models.IntegerField("Celular Hermano 5", blank=True, null=True,validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    tipo_via_hermano_5 = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_hermano_5 = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_principal_hermano_5 = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_hermano_5 = models.BooleanField("¿Bis?", default=False)
    letra_bis_hermano_5 = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_hermano_5 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_hermano_5 = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_secundaria_hermano_5 = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_hermano_5 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_hermano_5 = models.CharField("Número Final", max_length=30, blank=True, null=True)
    complemento_hermano_5 = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True)
    direccion_formateada_hermano_5 = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = "Dato Familiar"
        verbose_name_plural = "Datos Familiares"

#Es necesario completar esta parte para todas las direcciones, de lo contrario solo las va a construir pero no a guardar
    def __str__(self):
        return f"Datos Familiares {self.id}"
    @property
    def direccion_completa_conyugue(self):
        partes = [
            self.tipo_via_conyugue,
            self.numero_principal_conyugue,
            self.letra_principal_conyugue,
            "BIS" if self.bis_conyugue else "",
            self.letra_bis_conyugue,
            self.cuadrante_conyugue,
        ]

        if self.numero_secundario_conyugue:
            partes.extend([
                "#", self.numero_secundario_conyugue,
                self.letra_secundaria_conyugue, self.cuadrante_dos_conyugue
            ])

        partes.append(self.nro_conyugue)
        direccion = " ".join(filter(None, partes))
        if self.complemento_conyugue:
            direccion += f", {self.complemento_conyugue}"
        return direccion.strip()

    def save(self, *args, **kwargs):
        self.direccion_formateada_conyugue = self.direccion_completa_conyugue
        super().save(*args, **kwargs)



class Hijo(models.Model):
    
    datos_familiares = models.ForeignKey('DatosFamiliares', on_delete=models.CASCADE, related_name="hijos")

    nombre = models.CharField("Nombre del hijo", max_length=50)
    edad = models.IntegerField("Edad", validators=[MinValueValidator(0), MaxValueValidator(200)])
    identificacion = models.CharField("Identificación", max_length=20)

    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"
    
    
    

class InformacionAcademica(models.Model):
    recluta = models.ForeignKey('Recluta', on_delete=models.CASCADE, related_name='informaciones_academicas',null=True)

#Estudios 1
    estudios_1 = models.CharField("Estudios Realizados 1", max_length=50, blank=True, null=True)
    año_estudios_1 = models.IntegerField("Año",blank=True,null=True,validators=[MinValueValidator(1900), MaxValueValidator(2030)])
    titulo_estudios_1 = models.CharField("Título Recibido", max_length=50,blank=True,null=True) 
    nombre_institucion_estudios_1 = models.CharField("Nombre de la Institución", max_length=70, blank=True,null=True)
    ciudad_estudios_1 = models.CharField("Ciudad", max_length=50, blank=True,null=True)
#Estudios 2
    estudios_2 = models.CharField("Estudios Realizados 2", max_length=50, blank=True, null=True)
    año_estudios_2 = models.IntegerField("Año",blank=True,null=True,validators=[MinValueValidator(1900), MaxValueValidator(2030)])
    titulo_estudios_2 = models.CharField("Título Recibido", max_length=50,blank=True,null=True) 
    nombre_institucion_estudios_2 = models.CharField("Nombre de la Institución", max_length=70, blank=True,null=True)
    ciudad_estudios_2 = models.CharField("Ciudad", max_length=50, blank=True,null=True)
#Estudios 3
    estudios_3 = models.CharField("Estudios Realizados 3", max_length=50, blank=True, null=True)
    año_estudios_3 = models.IntegerField("Año",blank=True,null=True,validators=[MinValueValidator(1900), MaxValueValidator(2030)])
    titulo_estudios_3 = models.CharField("Título Recibido", max_length=50,blank=True,null=True) 
    nombre_institucion_estudios_3 = models.CharField("Nombre de la Institución", max_length=70, blank=True,null=True)
    ciudad_estudios_3 = models.CharField("Ciudad", max_length=50, blank=True,null=True)
#Estudios 4
    estudios_4 = models.CharField("Estudios Realizados 4", max_length=50, blank=True, null=True)
    año_estudios_4 = models.IntegerField("Año",blank=True,null=True,validators=[MinValueValidator(1900), MaxValueValidator(2030)])
    titulo_estudios_4 = models.CharField("Título Recibido", max_length=50,blank=True,null=True) 
    nombre_institucion_estudios_4 = models.CharField("Nombre de la Institución", max_length=70, blank=True,null=True)
    ciudad_estudios_4 = models.CharField("Ciudad", max_length=50, blank=True,null=True)
#Idiomas Extranjeros 1
    idioma_extranjero_1 = models.CharField("Idioma extranjero 1", max_length=50,blank=True,null=True)
    lee_idioma_extranjero_1 = models.CharField("¿Lee?",null=True,blank=True,choices=[("Sí","Sí"),("No","No")])
    habla_idioma_extranjero_1 = models.CharField("¿Habla?",null=True,blank=True,choices=[("Sí","Sí"),("No","No")])
    escribe_idioma_extranjero_1 = models.CharField("¿Escribe?",null=True,blank=True,choices=[("Sí","Sí"),("No","No")])
#Idiomas Extranjeros 2
    idioma_extranjero_2 = models.CharField("Idioma extranjero 2", max_length=50,blank=True,null=True)
    lee_idioma_extranjero_2 = models.CharField("¿Lee?",null=True,blank=True,choices=[("Sí","Sí"),("No","No")])
    habla_idioma_extranjero_2 = models.CharField("¿Escribe?",null=True,blank=True,choices=[("Sí","Sí"),("No","No")])
    escribe_idioma_extranjero_2 = models.CharField("¿Escribe?",null=True,blank=True,choices=[("Sí","Sí"),("No","No")])
#Ofimática
    word_check = models.CharField("Word",null=True,choices=[("Sí","Sí"),("No","No")])
    excel_check = models.CharField("Excel",null=True,choices=[("Sí","Sí"),("No","No")])
    powerpoint_check = models.CharField("Power Point",null=True,choices=[("Sí","Sí"),("No","No")])
    access_check = models.CharField("Access",null=True,choices=[("Sí","Sí"),("No","No")])
    internet_check = models.CharField("Internet",null=True,choices=[("Sí","Sí"),("No","No")])
    otro_check= models.CharField("Otros (Separe por comas)", null=True,blank=True,max_length=333)

    class Meta:
        verbose_name = "Información Académica"
        verbose_name_plural = "Informaciones Académicas"

    def __str__(self):
        return f"Información académica {self.id}"

class ReferenciasPersonales(models.Model):
    recluta = models.ForeignKey('Recluta', on_delete=models.CASCADE, related_name='referencias_personales',null=True)

#Referencia 1
    nombre_referencia_1 = models.CharField("Nombres y apellidos",max_length=333,null=True)
    ocupacion_referencia_1 = models.CharField("Ocupación",max_length=333,null=True)
    empresa_referencia_1 = models.CharField("Empresa",max_length=333,null=True,blank=True)
    tiempo_referencia_1 = models.IntegerField("Tiempo de Conocido (Años)",null=True, validators=[MinValueValidator(0), MaxValueValidator(333)])
    ciudad_referencia_1 = models.CharField("Ciudad",max_length=333,null=True)
    telefono_referencia_1 = models.IntegerField("Teléfono",null=True, validators=[MinValueValidator(100000), MaxValueValidator(999_999_999_999)])

    tipo_via_referencia_1 = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_referencia_1 = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_principal_referencia_1 = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_referencia_1 = models.BooleanField("¿Bis?", default=False)
    letra_bis_referencia_1 = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_referencia_1 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_referencia_1 = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_secundaria_referencia_1 = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_referencia_1 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_referencia_1 = models.CharField("Número Final", max_length=30, blank=True, null=True)
    complemento_referencia_1 = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True)
    
    direccion_formateada_referencia_1 = models.CharField(max_length=500, blank=True, null=True)

#Referencia 2
   

    nombre_referencia_2 = models.CharField("Nombres y apellidos",max_length=333,null=True)
    ocupacion_referencia_2 = models.CharField("Ocupación",max_length=333,null=True)
    empresa_referencia_2 = models.CharField("Empresa",max_length=333,null=True,blank=True)
    tiempo_referencia_2 = models.IntegerField("Tiempo de Conocido (Años)",null=True, validators=[MinValueValidator(0), MaxValueValidator(333)])
    ciudad_referencia_2 = models.CharField("Ciudad",max_length=333,null=True)
    telefono_referencia_2 = models.IntegerField("Teléfono",null=True, validators=[MinValueValidator(100000), MaxValueValidator(999_999_999_999)])

    tipo_via_referencia_2 = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_referencia_2 = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_principal_referencia_2 = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_referencia_2 = models.BooleanField("¿Bis?", default=False)
    letra_bis_referencia_2 = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_referencia_2 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_referencia_2 = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_secundaria_referencia_2 = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_referencia_2 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_referencia_2 = models.CharField("Número Final", max_length=30, blank=True, null=True)
    complemento_referencia_2 = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True)
    direccion_formateada_referencia_2 = models.CharField(max_length=500, blank=True, null=True)

#Referencia 3

    nombre_referencia_3 = models.CharField("Nombres y apellidos",max_length=333,null=True)
    ocupacion_referencia_3 = models.CharField("Ocupación",max_length=333,null=True)
    empresa_referencia_3 = models.CharField("Empresa",max_length=333,null=True,blank=True)
    tiempo_referencia_3 = models.IntegerField("Tiempo de Conocido (Años)",null=True, validators=[MinValueValidator(0), MaxValueValidator(333)])
    ciudad_referencia_3 = models.CharField("Ciudad",max_length=333,null=True)
    telefono_referencia_3 = models.IntegerField("Teléfono",null=True, validators=[MinValueValidator(100000), MaxValueValidator(999_999_999_999)])

    tipo_via_referencia_3  = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_referencia_3  = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_principal_referencia_3  = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_referencia_3  = models.BooleanField("¿Bis?", default=False)
    letra_bis_referencia_3  = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_referencia_3  = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_referencia_3  = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_secundaria_referencia_3  = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_referencia_3  = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_referencia_3  = models.CharField("Número Final", max_length=30, blank=True, null=True)
    complemento_referencia_3  = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True)
    
    direccion_formateada_referencia_3 = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = "Referencias Personales"
        verbose_name_plural = "Referencias Personales"

    def __str__(self):
        return f"Referencias Personales {self.id}"

class SectorDefensa(models.Model):
    recluta = models.ForeignKey('Recluta', on_delete=models.CASCADE, related_name='sector_defensa',null=True)
#Amigos y familiares que trabajan en sector defensa 1

    nombresyapellidos_sd_1 = models.CharField("Nombres y apellidos",max_length=333,null=True,blank=True)
    cargo_sd_1 = models.CharField("Cargo", max_length=60,null=True,blank=True)
    entidad_sd_1 = models.CharField("Entidad u Organismo",max_length=333,null=True,blank=True)
    unidad_militar_sd_1 = models.CharField("Unidad Militar", max_length=333,null=True,blank=True)
    celular_sd_1 = models.IntegerField("Teléfono Celular", null=True,blank=True)

    tipo_via_sd_1  = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_sd_1  = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_principal_sd_1  = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_sd_1  = models.BooleanField("¿Bis?", default=False)
    letra_bis_sd_1  = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_sd_1  = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_sd_1  = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_secundaria_sd_1  = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_sd_1  = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_sd_1  = models.CharField("Número Final", max_length=30, blank=True, null=True)
    complemento_sd_1  = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True)
    direccion_formateada_sd_1 = models.CharField(max_length=500, blank=True, null=True)

#Amigos y familiares que trabajan en sector defensa 2

    nombresyapellidos_sd_2 = models.CharField("Nombres y apellidos",max_length=333,null=True,blank=True)
    cargo_sd_2 = models.CharField("Cargo", max_length=60,null=True,blank=True)
    entidad_sd_2 = models.CharField("Entidad u Organismo",max_length=333,null=True,blank=True)
    unidad_militar_sd_2 = models.CharField("Unidad Militar", max_length=333,null=True,blank=True)
    celular_sd_2 = models.IntegerField("Teléfono Celular", null=True,blank=True,validators=[MinValueValidator(100000), MaxValueValidator(999_999_999_999)])

    tipo_via_sd_2  = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_sd_2  = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_principal_sd_2  = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_sd_2  = models.BooleanField("¿Bis?", default=False)
    letra_bis_sd_2  = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_sd_2  = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_sd_2  = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_secundaria_sd_2  = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_sd_2  = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_sd_2  = models.CharField("Número Final", max_length=30, blank=True, null=True)
    complemento_sd_2  = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True)
    direccion_formateada_sd_2 = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = "Sector Defensa"
        verbose_name_plural = "Sector Defensa"

    def __str__(self):
        return f"Sector Defensa {self.id}"

class BienesRentasAEP(models.Model):
    recluta = models.ForeignKey('Recluta', on_delete=models.CASCADE, related_name='bienes_rentas',null=True)
    salarios_y_demas_ingresos_laborales = models.IntegerField("Salarios y demás ingresos laborales", null=True, blank=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999)])
    cesantías_e_intereses_de_cesantías = models.IntegerField("Cesantías e intereses de cesantías", null=True, blank=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999)])
    gastos_de_representación = models.IntegerField("Gastos de representación", null=True, blank=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999)])
    arriendos = models.IntegerField("Arriendos", null=True, blank=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999)])
    honorarios = models.IntegerField("Honorarios", null=True, blank=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999)])
    otros_ingresos_y_rentas = models.IntegerField("Otros ingresos y rentas", null=True, blank=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999)])

#CUENTAS EN COLOMBIA Y EL EXTERIOR

    entidad_financiera_1 = models.CharField("Entidad Financiera 1", blank=True,null=True,max_length=60)
    tipo_de_cuenta_1 = models.CharField("Tipo de cuenta 1", blank=True,null=True,max_length=60)
    numero_de_cuenta_1 = models.IntegerField("Numero de cuenta 1",blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])

    entidad_financiera_2 = models.CharField("Entidad Financiera 2", blank=True,null=True,max_length=60)
    tipo_de_cuenta_2 = models.CharField("Tipo de cuenta 2", blank=True,null=True,max_length=60)
    numero_de_cuenta_2 = models.IntegerField("Numero de cuenta 2",blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])

    entidad_financiera_3 = models.CharField("Entidad Financiera 3", blank=True,null=True,max_length=60)
    tipo_de_cuenta_3 = models.CharField("Tipo de cuenta 3", blank=True,null=True,max_length=60)
    numero_de_cuenta_3 = models.IntegerField("Numero de cuenta 3",blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])

    entidad_financiera_4 = models.CharField("Entidad Financiera 4", blank=True,null=True,max_length=60)
    tipo_de_cuenta_4 = models.CharField("Tipo de cuenta 4", blank=True,null=True,max_length=60)
    numero_de_cuenta_4 = models.IntegerField("Numero de cuenta 4",blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])

    entidad_financiera_5 = models.CharField("Entidad Financiera 5", blank=True,null=True,max_length=60)
    tipo_de_cuenta_5 = models.CharField("Tipo de cuenta 5", blank=True,null=True,max_length=60)
    numero_de_cuenta_5 = models.IntegerField("Numero de cuenta 5",blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])

    entidad_financiera_6 = models.CharField("Entidad Financiera 6", blank=True,null=True,max_length=60)
    tipo_de_cuenta_6 = models.CharField("Tipo de cuenta 6", blank=True,null=True,max_length=60)
    numero_de_cuenta_6 = models.IntegerField("Numero de cuenta 6",blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])

#BIENES PATRIMONIALES
    
    tipo_bien_1 = models.CharField("Tipo de bien 1", blank=True,null=True,max_length=333)
    ubicacion_bien_1 = models.CharField("Ubicación del bien 1 (Ciudad)",blank=True,null=True,max_length=333)
    identificacion_bien_1 = models.CharField("Identificación del bien 1", blank=True,null=True, max_length=333)
    avaluo_comercial_bien_1 = models.IntegerField("Avalúo comercial del bien 1",blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])

    tipo_bien_2 = models.CharField("Tipo de bien 2", blank=True,null=True,max_length=333)
    ubicacion_bien_2 = models.CharField("Ubicación del bien 2 (Ciudad)",blank=True,null=True,max_length=333)
    identificacion_bien_2 = models.CharField("Identificación del bien 2", blank=True,null=True, max_length=333)
    avaluo_comercial_bien_2 = models.IntegerField("Avalúo comercial del bien 2",blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])

    tipo_bien_3 = models.CharField("Tipo de bien 3", blank=True,null=True,max_length=333)
    ubicacion_bien_3 = models.CharField("Ubicación del bien 3 (Ciudad)",blank=True,null=True,max_length=333)
    identificacion_bien_3 = models.CharField("Identificación del bien 3", blank=True,null=True, max_length=333)
    avaluo_comercial_bien_3 = models.IntegerField("Avalúo comercial del bien 3",blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])

    tipo_bien_4 = models.CharField("Tipo de bien 4", blank=True,null=True,max_length=333)
    ubicacion_bien_4 = models.CharField("Ubicación del bien 4 (Ciudad)",blank=True,null=True,max_length=333)
    identificacion_bien_4 = models.CharField("Identificación del bien 4", blank=True,null=True, max_length=333)
    avaluo_comercial_bien_4 = models.IntegerField("Avalúo comercial del bien 4",blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])

    tipo_bien_5 = models.CharField("Tipo de bien 5", blank=True,null=True,max_length=333)
    ubicacion_bien_5 = models.CharField("Ubicación del bien 5 (Ciudad)",blank=True,null=True,max_length=333)
    identificacion_bien_5 = models.CharField("Identificación del bien 5", blank=True,null=True, max_length=333)
    avaluo_comercial_bien_5 = models.IntegerField("Avalúo comercial del bien 5",blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])

#OBLIGACIONES A LA FECHA
    entidad_o_persona_obligacion_1 = models.CharField("Entidad o persona", blank=True, null=True,max_length=333)
    concepto_obligacion_1 = models.CharField("Concepto", blank=True, null=True,max_length=333)
    valor_1 = models.IntegerField("Valor" ,blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])

    entidad_o_persona_obligacion_2 = models.CharField("Entidad o persona", blank=True, null=True,max_length=333)
    concepto_obligacion_2 = models.CharField("Concepto", blank=True, null=True,max_length=333)
    valor_2 = models.IntegerField("Valor" ,blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])


    entidad_o_persona_obligacion_3 = models.CharField("Entidad o persona", blank=True, null=True,max_length=333)
    concepto_obligacion_3 = models.CharField("Concepto", blank=True, null=True,max_length=333)
    valor_3 = models.IntegerField("Valor" ,blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])

    entidad_o_persona_obligacion_4 = models.CharField("Entidad o persona", blank=True, null=True,max_length=333)
    concepto_obligacion_4= models.CharField("Concepto", blank=True, null=True,max_length=333)
    valor_4 = models.IntegerField("Valor" ,blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])

#Participación en organizaciones, corporaciones, sociedades, asociaciones,ongs...
    entidad_o_institucion_1 = models.CharField("Entidad o institución 1", blank=True,null=True,max_length=333)
    calidad_de_miembro_1 = models.CharField("Calidad de miembro 1", blank=True,null=True,max_length=333)
    entidad_o_institucion_2 = models.CharField("Entidad o institución 2", blank=True,null=True,max_length=333)
    calidad_de_miembro_2 = models.CharField("Calidad de miembro 2", blank=True,null=True,max_length=333)
    entidad_o_institucion_3 = models.CharField("Entidad o institución 3", blank=True,null=True,max_length=333)
    calidad_de_miembro_3 = models.CharField("Calidad de miembro 3", blank=True,null=True,max_length=333)
    entidad_o_institucion_4 = models.CharField("Entidad o institución 4 ", blank=True,null=True,max_length=333)
    calidad_de_miembro_4 = models.CharField("Calidad de miembro 4", blank=True,null=True,max_length=333)

#ACTIVIDAD ECONÓMICA PRIVADA DEL ASPIRANTE
    empresa_1 = models.CharField("Empresa 1",blank=True,null=True,max_length=333)
    calidad_de_miembro_AEP_1 = models.CharField("Calidad de miembro 1",blank=True,null=True,max_length=333)
    empresa_2 = models.CharField("Empresa 2",blank=True,null=True,max_length=333)
    calidad_de_miembro_AEP_2 = models.CharField("Calidad de miembro 2",blank=True,null=True,max_length=333)
    empresa_3 = models.CharField("Empresa 3",blank=True,null=True,max_length=333)
    calidad_de_miembro_AEP_3 = models.CharField("Calidad de miembro 3",blank=True,null=True,max_length=333)

    class Meta:
        verbose_name = "Bienes y Rentas AEP"
        verbose_name_plural = "Bienes y Rentas AEP"

    def __str__(self):
        return f"Bienes y Rentas AEP {self.id}"

class SituacionJuridica(models.Model):
    recluta = models.ForeignKey('Recluta', on_delete=models.CASCADE, related_name='situaciones_juridicas',null=True)
#SITUACIÓN JURÍDICA
    fecha_proceso_1 = models.DateField("Fecha Proceso 1", blank=True, null=True)
    tipo_de_investigacion_1 = models.CharField("Tipo de Investigación 1", blank=True,null=True,max_length=333)
    causa_1 = models.CharField("Causa 1", blank=True,null=True,max_length=333)
    autoridad_1 = models.CharField("Autoridad 1", blank=True,null=True,max_length=333)
    estado_del_proceso_1 = models.CharField("Estado del Proceso 1", blank=True,null=True,max_length=333)
    responsable_1 = models.CharField("¿Responsable?", blank=True,null=True,max_length=333,choices=[("Sí","Sí"),("No","No")])

    fecha_proceso_2 = models.DateField("Fecha Proceso 2", blank=True, null=True)
    tipo_de_investigacion_2 = models.CharField("Tipo de Investigación 2", blank=True,null=True,max_length=333)
    causa_2 =  models.CharField("Causa 2", blank=True,null=True,max_length=333)
    autoridad_2 = models.CharField("Autoridad 2", blank=True,null=True,max_length=333)
    estado_del_proceso_2 = models.CharField("Estado del Proceso 2", blank=True,null=True,max_length=333)
    responsable_2 = models.CharField("¿Responsable?", blank=True,null=True,max_length=333,choices=[("Sí","Sí"),("No","No")])
    
    def __str__(self):
        return f"Situación Jurídica {self.id}"

class OtrosDatos(models.Model):
    recluta = models.ForeignKey('Recluta', on_delete=models.CASCADE, related_name='otros_datos',null=True)
    fecha_viaje_1 = models.DateField("Fecha Viaje 1",null=True,blank=True)
    pais_visitado_1 = models.CharField("País Visitado 1", null=True,blank=True,max_length=333)
    motivo_1 = models.CharField ("Motivo del viaje 1", null=True,blank=True,max_length=333)
    permanencia_1 = models.CharField("Tiempo de permanencia 1",null=True,blank=True,max_length=333)

    fecha_viaje_2 = models.DateField("Fecha Viaje 2",null=True,blank=True)
    pais_visitado_2 = models.CharField("País Visitado 2", null=True,blank=True,max_length=333)
    motivo_2 = models.CharField ("Motivo del viaje 2", null=True,blank=True,max_length=333)
    permanencia_2 = models.CharField("Tiempo de permanencia 2",null=True,blank=True,max_length=333)

    fecha_viaje_3 = models.DateField("Fecha Viaje 3",null=True,blank=True)
    pais_visitado_3 = models.CharField("País Visitado 3", null=True,blank=True,max_length=333)
    motivo_3 = models.CharField ("Motivo del viaje 3", null=True,blank=True,max_length=333)
    permanencia_3 = models.CharField("Tiempo de permanencia 3",null=True,blank=True,max_length=333)

    recomendante = models.CharField("Por quién tuvo conocimiento de este empleo?", null=True,blank=True,max_length=333)
    celular_recomendante = models.IntegerField("Celular de quien recomendó", blank=True, null=True, validators=[MinValueValidator(100000), MaxValueValidator(999_999_999_999)])
    labora_en_indumil = models.CharField("Lo recomienda alguien que labora en la empresa?",blank=True,null=True,choices=[("Sí","Sí"),("No","No")])
    nombres_y_apellidos_recomendante_1 = models.CharField("Nombres y apellidos 1",null=True,blank=True,max_length=333)
    nombres_y_apellidos_recomendante_2 = models.CharField("Nombres y apellidos 2",null=True,blank=True,max_length=333)
    cargo_recomendante_1 = models.CharField("Cargo Recomendante 1",null=True,blank=True,max_length=333)
    cargo_recomendante_2 = models.CharField("Cargo Recomendante 2",null=True,blank=True,max_length=333)
    unidad_negocio_recomendante_1 = models.CharField("Unidad de Negocio Recomendante 1",null=True,blank=True,max_length=333)
    unidad_negocio_recomendante_2 = models.CharField("Unidad de Negocio Recomendante 2",null=True,blank=True,max_length=333)

    tipo_via_recomendante = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_recomendante = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_principal_recomendante = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_recomendante = models.BooleanField("¿Bis?", default=False)
    letra_bis_recomendante = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_recomendante = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_recomendante = models.CharField("Número", max_length=10, null=True, blank=True)
    letra_secundaria_recomendante = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_recomendante = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_recomendante = models.CharField("Número Final", max_length=30, blank=True, null=True)
    complemento_recomendante = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True)
    razon_de_vinculo = models.TextField("Explique brevemente la razón por la cual desea vincularse con la empresa:", max_length=1_123_581_321, null=True)
    direccion_formateada_recomendante = models.CharField(max_length=500, blank=True, null=True)


    class Meta:
        verbose_name = "Otros Datos"
        verbose_name_plural = "Otros Datos"
    
    def __str__(self):
        return f"Otros Datos {self.id}"

class DocumentoGenerado(models.Model):
    recluta = models.ForeignKey(Recluta, on_delete=models.CASCADE, related_name="documentos")
    tipo = models.CharField(max_length=50)
    archivo = models.FileField(upload_to="documentos/%Y/%m/")
    

    def __str__(self):
        return f"{self.tipo} de {self.recluta}"

