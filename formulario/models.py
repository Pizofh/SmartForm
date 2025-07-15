
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator

# --- Validadores REGEX ---

only_letters = RegexValidator(r'^[A-Za-zÁÉÍÓÚÑáéíóúñ ]+$', 'Solo se permiten letras y espacios.')
alphanumeric = RegexValidator(r'^[A-Za-zÁÉÍÓÚÑáéíóúñ0-9 ]+$','Solo se permiten letras, números y espacios.')
simple_text = RegexValidator(r'^[A-Za-zÁÉÍÓÚÑÜüöÖäÄáéíóúñ0-9\s.,¨:#-]*$','Solo letras (incluyendo diéresis), números, espacios y signos básicos.')
only_numbers = RegexValidator(r'^\d+$', 'Solo se permiten números.')

class PersonalData(models.Model):
    """
    Modelo que representa la información personal, de identificación, y de contacto
    de una persona que se registra como recluta en el sistema.

    Contempla múltiples campos, incluyendo nombre completo, documentos de identidad,
    datos de nacimiento, libreta militar, características físicas, dirección detallada
    y redes sociales. Se aplica validación en campos clave para garantizar integridad
    y unicidad.
    """ 

    # --- Información personal ---
    first_name = models.CharField(max_length=30,validators=[only_letters])
    second_name = models.CharField(max_length=30, blank=True,validators=[only_letters])
    lastname = models.CharField(max_length=80,validators=[only_letters])
    second_lastname = models.CharField(max_length=80, blank=True,validators=[only_letters])

    # --- Documentos de identidad ---
    document_type = models.CharField(
        "Tipo de documento", max_length=2,
        choices=[("CC", "Cédula Ciudadanía"), ("CE", "Cédula Extranjería")]
    )
    document_number = models.IntegerField("Número de documento", unique=True,validators=[MinValueValidator(1_000), MaxValueValidator(99_999_999_999)])
    expedition_date = models.DateField("Fecha de expedición de la cédula")
    expedition_place = models.CharField("Lugar de expedición", max_length=20,validators=[only_letters])
    passport_number = models.CharField("Pasaporte No", max_length=12, blank=True,validators=[alphanumeric])
    passport_date = models.DateField("Fecha de expedición del pasaporte", null=True, blank=True)

    # --- Fecha de nacimiento (distribuida por partes) ---
    dia_nacimiento = models.IntegerField("Día de nacimiento", null=True, choices=[(i, str(i)) for i in range(1, 32)])
    mes_nacimiento = models.CharField(
        "Mes de nacimiento", max_length=13, null=True,
        choices=[(str(i), mes) for i, mes in enumerate([
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ], start=1)]
    )
    año_nacimiento = models.IntegerField("Año de Nacimiento", null=True,
                                         validators=[MinValueValidator(1900), MaxValueValidator(2025)])

    # --- Estado civil y profesión ---
    estado_civil = models.CharField(
        "Estado Civil", max_length=30, null=True,
        choices=[
            ("Casado(a)", "Casado(a)"), ("Soltero(a)", "Soltero(a)"),
            ("Unión Marital de Hecho", "Unión Marital de Hecho"),
            ("Separado de Hecho", "Separado de Hecho"), ("Divorciado(a)", "Divorciado(a)"), ("Viudo(a)", "Viudo(a)")
        ]
    )
    profesion_oficio = models.CharField("Profesión u Oficio", max_length=30, null=True,validators=[only_letters])
    tarjeta_profesional = models.CharField("Tarjeta profesional", max_length=15, null=True,validators=[alphanumeric])
    señales_corporales = models.CharField("Señales corporales", max_length=50, null=True,validators=[simple_text])
    estatura = models.IntegerField("Estatura (cm)", null=True,
                                   validators=[MinValueValidator(80), MaxValueValidator(400)])
    peso = models.IntegerField("Peso (kg)", null=True,
                               validators=[MinValueValidator(10), MaxValueValidator(500)])

    # --- Dirección (estructura desglosada) ---
    tipo_via = models.CharField("Tipo de vía", max_length=20, null=True,
                                choices=[('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'),
                                         ('Avenida', 'Avenida'), ('Avenida Calle', 'Avenida Calle'),
                                         ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
                                         ('Callejón', 'Callejón'), ('Carrera', 'Carrera'),
                                         ('Circular', 'Circular'), ('Diagonal', 'Diagonal'),
                                         ('Transversal', 'Transversal')])
    numero_principal = models.CharField("Número",max_length=10,null=True,validators=[only_numbers])
    letra_principal = models.CharField("Letra", max_length=2, null=True, blank=True,
                                       choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis = models.BooleanField("¿Bis?", default=False)
    letra_bis = models.CharField("Letra Bis", max_length=2, blank=True, null=True,
                                 choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante = models.CharField("Cuadrante", max_length=10,
                                 choices=[('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')],
                                 blank=True, null=True)
    numero_secundario = models.CharField("Número",max_length=10, null=True,validators=[only_numbers])
    letra_secundaria = models.CharField("Letra", max_length=2, blank=True, null=True,
                                        choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos = models.CharField("Cuadrante", max_length=10,
                                     choices=[('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')],
                                     blank=True, null=True)
    nro = models.CharField("Número Final", max_length=30, blank=True, null=True,validators=[only_numbers])
    complemento = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True,validators=[simple_text])
    barrio = models.CharField("Barrio", max_length=50, null=True,validators=[alphanumeric])
 
    # --- Contacto ---
    numero_celular = models.IntegerField("Número celular", unique=True, null=True,
                                         validators=[MinValueValidator(1_000), MaxValueValidator(99_999_999_999)])
    telefono_fijo = models.IntegerField("Numero de teléfono fijo", blank=True, null=True,
                                        validators=[MinValueValidator(1_000), MaxValueValidator(99_999_999_999)])
    ciudad = models.CharField("Ciudad de nacimiento", max_length=30, null=True,validators=[only_letters])
    departamento = models.CharField("Departamento de nacimiento", max_length=30, null=True,validators=[only_letters])
    correo_electronico_personal = models.EmailField("Correo Electrónico Personal", null=True)

    # Dirección generada automáticamente
    direccion_formateada = models.CharField(max_length=500, blank=True, null=True,validators=[simple_text])

    class Meta:
        verbose_name = "PersonalData"
        verbose_name_plural = "PersonalData"

    @property
    def nombres(self):
        """
        Devuelve el nombre completo concatenado, omitiendo espacios innecesarios.
        """
        return f"{self.first_name} {self.second_name}".strip()

    @property
    def apellidos(self):
        """
        Devuelve los apellidos concatenados, omitiendo espacios innecesarios.
        """
        return f"{self.lastname} {self.second_lastname}".strip()

    @property
    def direccion_completa(self):
        """
        Construye y devuelve la dirección del recluta de manera estructurada y legible.
        """
        partes = [
            self.tipo_via,
            self.numero_principal,
            self.letra_principal,
            "BIS" if self.bis else "",
            self.letra_bis,
            self.cuadrante,
        ]
        if self.numero_secundario:
            partes.extend(["#", self.numero_secundario, self.letra_secundaria, self.cuadrante_dos])
        partes.append(self.nro)
        direccion = " ".join(filter(None, partes))
        if self.complemento:
            direccion += f", {self.complemento}"
        return direccion.strip()

    def save(self, *args, **kwargs):
        """
        Al guardar el modelo, genera automáticamente la dirección formateada
        usando los campos de dirección desglosada.
        """
        self.direccion_formateada = self.direccion_completa
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Devuelve una representación legible del objeto (nombre completo).
        """
        return f"{self.nombres} {self.apellidos}"



class DatosFamiliares(models.Model):

    """
    Modelo que almacena información familiar detallada del recluta.

    Contiene los datos del cónyuge, padre y madre, incluyendo nombres, identificación,
    teléfonos, profesión y dirección. Las direcciones siguen el mismo desglose estructurado
    usado en el modelo principal de Recluta.

    Se relaciona 1:1 con un único objeto Recluta.

    Attributes:
        recluta (OneToOneField): Relación directa con el modelo Recluta.
        nombre_conyugue (CharField): Nombre completo del cónyuge.
        cedula_conyugue (CharField): Cédula del cónyuge.
        ... (continúan atributos similares para padre y madre)
    """

    # Relación directa con Recluta (uno a uno)
    PersonalData = models.OneToOneField(PersonalData, on_delete=models.CASCADE, null=True)

    # --- Datos del cónyuge ---
    nombre_conyugue = models.CharField("Nombre del Cónyugue", max_length=50, blank=True,validators=[only_letters])
    cedula_conyugue = models.IntegerField("Cédula del Cónyugue", validators=[MinValueValidator(1_000), MaxValueValidator(999_999_999_999)], blank=True, null=True)
    profesion_oficio_conyugue = models.CharField("Profesión del Cónyugue", max_length=50, blank=True, null=True,validators=[only_letters])
    celular_conyugue = models.IntegerField("Celular del Cónyugue", max_length=15, blank=True,validators=[MinValueValidator(1_000), MaxValueValidator(999_999_999_999)])
    tipo_via_conyugue = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_conyugue = models.CharField("Número", max_length=10, null=True, blank=True,validators=[only_numbers])
    letra_principal_conyugue = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_conyugue = models.BooleanField("¿Bis?", default=False)
    letra_bis_conyugue = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_conyugue = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_conyugue = models.CharField("Número", max_length=10, null=True, blank=True,validators=[only_numbers])
    letra_secundaria_conyugue = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_conyugue = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_conyugue = models.CharField("Número Final", max_length=30, blank=True, null=True,validators=[only_numbers])
    complemento_conyugue = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True,validators=[simple_text])
    direccion_formateada_conyugue = models.CharField(max_length=500, blank=True, null=True,validators=[simple_text])

    # --- Datos del padre ---
    nombre_padre = models.CharField("Nombre del padre", max_length=55, null=True,validators=[only_letters])
    vive_padre = models.CharField("¿Vive?", null=True, choices=[("Sí", "Sí"), ("No", "No")])
    identificación_padre = models.IntegerField("CC No", null=True, validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    telefono_padre = models.IntegerField("Teléfono del Padre", blank=True, null=True, validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    oficio_profesion_padre = models.CharField("Profesión u Oficio", blank=True, null=True, max_length=50,validators=[only_letters])

    tipo_via_padre = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_padre = models.CharField("Número", max_length=10, null=True, blank=True,validators=[only_numbers])
    letra_principal_padre = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_padre = models.BooleanField("¿Bis?", default=False)
    letra_bis_padre = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_padre = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_padre = models.CharField("Número", max_length=10, null=True, blank=True,validators=[only_numbers])
    letra_secundaria_padre = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_padre = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_padre = models.CharField("Número Final", max_length=30, blank=True, null=True,validators=[only_numbers])
    complemento_padre = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True,validators=[simple_text])
    direccion_formateada_padre = models.CharField(max_length=500, blank=True, null=True,validators=[simple_text])

    # --- Datos de la madre ---
    nombre_madre = models.CharField("Nombre del madre", max_length=55, null=True,validators=[only_letters])
    vive_madre = models.CharField("¿Vive?", null=True, choices=[("Sí", "Sí"), ("No", "No")])
    identificación_madre = models.IntegerField("CC No", null=True, validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    telefono_madre = models.IntegerField("Teléfono de la Madre", blank=True, null=True, validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    oficio_profesion_madre = models.CharField("Profesión u Oficio de la Madre", blank=True, null=True, max_length=50,validators=[only_letters])

    tipo_via_madre = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_madre = models.CharField("Número", max_length=10, null=True, blank=True,validators=[only_numbers])
    letra_principal_madre = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_madre = models.BooleanField("¿Bis?", default=False)
    letra_bis_madre = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_madre = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_madre = models.CharField("Número", max_length=10, null=True, blank=True,validators=[only_numbers])
    letra_secundaria_madre = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_madre = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_madre = models.CharField("Número Final", max_length=30, blank=True, null=True,validators=[only_numbers])
    complemento_madre = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True,validators=[simple_text])
    direccion_formateada_madre = models.CharField(max_length=500, blank=True, null=True,validators=[simple_text])

    class Meta:
        verbose_name = "Dato Familiar"
        verbose_name_plural = "Datos Familiares"

    def __str__(self):
        """
        Retorna una representación legible del objeto.

        Returns:
            str: Texto identificador con el ID del objeto.
        """
        return f"Datos Familiares {self.id}"

    @property
    def direccion_completa_conyugue(self):
        """
        Construye la dirección completa del cónyuge a partir de los campos desglosados.

        Returns:
            str: Dirección formateada del cónyuge.
        """
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
        """
        Al guardar el objeto, genera y guarda la dirección formateada del cónyuge.
        """
        self.direccion_formateada_conyugue = self.direccion_completa_conyugue
        super().save(*args, **kwargs)


class Hijo(models.Model):
    """
    Modelo que representa un hijo o hija del recluta, vinculado a través de los datos familiares.

    Cada hijo está relacionado con una instancia de `DatosFamiliares` y contiene
    su nombre, edad y número de identificación.

    Attributes:
        datos_familiares (ForeignKey): Relación muchos a uno con `DatosFamiliares`.
        nombre (CharField): Nombre del hijo.
        edad (IntegerField): Edad del hijo, validada para estar entre 0 y 200 años.
        identificacion (CharField): Número de identificación del hijo.
    """

    datos_familiares = models.ForeignKey(
        'DatosFamiliares',
        on_delete=models.CASCADE,
        related_name="hijos"
    )

    nombre = models.CharField("Nombre del hijo", max_length=50,validators=[only_letters])
    edad = models.IntegerField("Edad",validators=[MinValueValidator(0), MaxValueValidator(200)])
    identificacion = models.IntegerField("Identificación",validators=[MinValueValidator(0), MaxValueValidator(99999_999_999)])

    def __str__(self):
        """
        Retorna una representación legible del hijo, incluyendo nombre y edad.

        Returns:
            str: Nombre y edad del hijo, formateado para visualización.
        """
        return f"{self.nombre} ({self.edad} años)"
    

class Hermano(models.Model):
    """
    Modelo que representa a un hermano o hermana del recluta.

    Cada hermano está vinculado a un objeto `DatosFamiliares` y contiene
    información personal, de contacto y dirección estructurada, similar
    al modelo del recluta.

    Attributes:
        datos_familiares (ForeignKey): Relación con el modelo `DatosFamiliares`.
        primer_apellido_hermano (CharField): Primer apellido del hermano.
        segundo_apellido_hermano (CharField): Segundo apellido del hermano.
        primer_nombre_hermano (CharField): Primer nombre del hermano.
        segundo_nombre_hermano (CharField): Segundo nombre del hermano.
        identificacion_hermano (IntegerField): Número de identificación.
        ocupacion_hermano (CharField): Profesión u ocupación actual.
        celular_hermano (IntegerField): Número de celular de contacto.
        tipo_via_hermano, número_principal_hermano, etc.: Dirección desglosada del hermano.
        direccion_formateada_hermano (CharField): Dirección completa construida a partir de los campos anteriores.
    """

    datos_familiares = models.ForeignKey(
        'DatosFamiliares',
        on_delete=models.CASCADE,
        related_name="hermanos"
    )

    # Datos personales y contacto
    primer_apellido_hermano = models.CharField("Primer Apellido", blank=True, null=True, max_length=30,validators=[only_letters])
    segundo_apellido_hermano = models.CharField("Segundo Apellido", blank=True, null=True, max_length=30,validators=[only_letters])
    primer_nombre_hermano = models.CharField("Primer Nombre", blank=True, null=True, max_length=30,validators=[only_letters])
    segundo_nombre_hermano = models.CharField("Segundo Nombre", blank=True, null=True, max_length=30,validators=[only_letters])
    identificacion_hermano = models.IntegerField(
        "Identificación Hermano 1",
        blank=True, null=True,
        validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)]
    )
    ocupacion_hermano = models.CharField("Ocupación Hermano 1", blank=True, null=True, max_length=60,validators=[only_letters])
    celular_hermano = models.IntegerField(
        "Celular Hermano 1",
        blank=True, null=True,
        validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)]
    )

    # Dirección desglosada
    tipo_via_hermano = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal')
    ])
    numero_principal_hermano = models.CharField("Número", max_length=10, null=True, blank=True,validators=[only_numbers])
    letra_principal_hermano = models.CharField("Letra", max_length=2, null=True, blank=True, choices=[
        (chr(c), chr(c)) for c in range(65, 91)
    ])
    bis_hermano = models.BooleanField("¿Bis?", default=False)
    letra_bis_hermano = models.CharField("Letra Bis", max_length=2, blank=True, null=True, choices=[
        (chr(c), chr(c)) for c in range(65, 91)
    ])
    cuadrante_hermano = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_hermano = models.CharField("Número", max_length=10, null=True, blank=True,validators=[only_numbers])
    letra_secundaria_hermano = models.CharField("Letra", max_length=2, blank=True, null=True, choices=[
        (chr(c), chr(c)) for c in range(65, 91)
    ])
    cuadrante_dos_hermano = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_hermano = models.CharField("Número Final", max_length=30, blank=True, null=True,validators=[only_numbers])
    complemento_hermano = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True,validators=[simple_text])
    direccion_formateada_hermano = models.CharField(max_length=500, blank=True, null=True,validators=[simple_text])

    def __str__(self):
        """
        Retorna una representación legible del hermano para el admin o consola.

        Returns:
            str: Nombre y cédula del hermano en formato compacto.
        """
        return f"{self.primer_nombre_hermano or ''} {self.primer_apellido_hermano or ''} - {self.identificacion_hermano or ''}".strip()


class InformacionAcademica(models.Model):
    """
    Modelo que almacena la información académica y conocimientos en idiomas y ofimática de un recluta.

    Se incluyen hasta cuatro niveles de estudios formales, dos idiomas extranjeros con habilidades evaluadas
    (lectura, escritura, habla), y conocimientos en herramientas ofimáticas comunes como Word, Excel, etc.

    Attributes:
        recluta (ForeignKey): Relación con el modelo `Recluta`.
        estudios_X (CharField): Descripción de los estudios realizados en cada nivel.
        año_estudios_X (IntegerField): Año de finalización de los estudios.
        titulo_estudios_X (CharField): Título recibido.
        nombre_institucion_estudios_X (CharField): Nombre de la institución educativa.
        ciudad_estudios_X (CharField): Ciudad donde se realizaron los estudios.
        idioma_extranjero_X (CharField): Idioma extranjero declarado.
        lee_idioma_extranjero_X / habla_ / escribe_ (CharField): Habilidades lingüísticas evaluadas.
        word_check / excel_check / ... (CharField): Conocimientos en herramientas de ofimática.
        otro_check (CharField): Campo libre para declarar otras herramientas.
    """

    PersonalData = models.ForeignKey(
        'PersonalData',
        on_delete=models.CASCADE,
        related_name='informaciones_academicas',
        null=True
    )

    # --- Estudios formales (hasta 4 registros) ---
    estudios_1 = models.CharField("Estudios Realizados 1", max_length=50, blank=True, null=True,validators=[only_letters])
    año_estudios_1 = models.IntegerField("Año", blank=True, null=True,
                                         validators=[MinValueValidator(1900), MaxValueValidator(2030)])
    titulo_estudios_1 = models.CharField("Título Recibido", max_length=50, blank=True, null=True,validators=[simple_text])
    nombre_institucion_estudios_1 = models.CharField("Nombre de la Institución", max_length=70, blank=True, null=True,validators=[simple_text])
    ciudad_estudios_1 = models.CharField("Ciudad", max_length=50, blank=True, null=True,validators=[simple_text])

    estudios_2 = models.CharField("Estudios Realizados 2", max_length=50, blank=True, null=True,validators=[simple_text])
    año_estudios_2 = models.IntegerField("Año", blank=True, null=True,
                                         validators=[MinValueValidator(1900), MaxValueValidator(2030)])
    titulo_estudios_2 = models.CharField("Título Recibido", max_length=50, blank=True, null=True,validators=[simple_text])
    nombre_institucion_estudios_2 = models.CharField("Nombre de la Institución", max_length=70, blank=True, null=True,validators=[simple_text])
    ciudad_estudios_2 = models.CharField("Ciudad", max_length=50, blank=True, null=True,validators=[simple_text])


    # --- Idiomas extranjeros (hasta 2 idiomas) ---
    idioma_extranjero_1 = models.CharField("Idioma extranjero 1", max_length=50, blank=True, null=True,validators=[simple_text])
    lee_idioma_extranjero_1 = models.CharField("¿Lee?", null=True, blank=True, choices=[("Sí", "Sí"), ("No", "No")])
    habla_idioma_extranjero_1 = models.CharField("¿Habla?", null=True, blank=True, choices=[("Sí", "Sí"), ("No", "No")])
    escribe_idioma_extranjero_1 = models.CharField("¿Escribe?", null=True, blank=True, choices=[("Sí", "Sí"), ("No", "No")])

    idioma_extranjero_2 = models.CharField("Idioma extranjero 2", max_length=50, blank=True, null=True,validators=[simple_text])
    lee_idioma_extranjero_2 = models.CharField("¿Lee?", null=True, blank=True, choices=[("Sí", "Sí"), ("No", "No")])
    habla_idioma_extranjero_2 = models.CharField("¿Escribe?", null=True, blank=True, choices=[("Sí", "Sí"), ("No", "No")])
    escribe_idioma_extranjero_2 = models.CharField("¿Escribe?", null=True, blank=True, choices=[("Sí", "Sí"), ("No", "No")])

    # --- Conocimientos en herramientas ofimáticas ---
    word_check = models.CharField("Word", null=True, choices=[("Sí", "Sí"), ("No", "No")])
    excel_check = models.CharField("Excel", null=True, choices=[("Sí", "Sí"), ("No", "No")])
    powerpoint_check = models.CharField("Power Point", null=True, choices=[("Sí", "Sí"), ("No", "No")])
    access_check = models.CharField("Access", null=True, choices=[("Sí", "Sí"), ("No", "No")])
    internet_check = models.CharField("Internet", null=True, choices=[("Sí", "Sí"), ("No", "No")])
    otro_check = models.CharField("Otros (Separe por comas)", null=True, blank=True, max_length=333,validators=[simple_text])

    class Meta:
        verbose_name = "Información Académica"
        verbose_name_plural = "Informaciones Académicas"

    def __str__(self):
        """
        Retorna una representación textual de la instancia para el admin o consola.

        Returns:
            str: Texto identificador con el ID de la información académica.
        """
        return f"Información académica {self.id}"


class ReferenciasPersonales(models.Model):
    """
    Modelo que almacena hasta tres referencias personales del recluta.

    Para cada referencia, se recopila su nombre completo, ocupación, empresa,
    tiempo de conocimiento, ciudad, teléfono y dirección estructurada. Cada
    instancia de este modelo está relacionada con un objeto `Recluta`.

    Attributes:
        recluta (ForeignKey): Relación con el modelo `Recluta`.
        nombre_referencia_X (CharField): Nombres y apellidos de la referencia.
        ocupacion_referencia_X (CharField): Ocupación o cargo.
        empresa_referencia_X (CharField): Empresa donde trabaja o ha trabajado.
        tiempo_referencia_X (IntegerField): Años de conocimiento.
        ciudad_referencia_X (CharField): Ciudad de residencia.
        telefono_referencia_X (IntegerField): Teléfono de contacto.
        tipo_via_referencia_X ... complemento_referencia_X: Componentes de la dirección.
        direccion_formateada_referencia_X (CharField): Dirección completa como texto libre.
    """

    PersonalData = models.ForeignKey(
        'PersonalData',
        on_delete=models.CASCADE,
        related_name='referencias_personales',
        null=True
    )

    # --- Referencia 1 ---
    nombre_referencia_1 = models.CharField("Nombres y apellidos", max_length=333, null=True,validators=[only_letters])
    ocupacion_referencia_1 = models.CharField("Ocupación", max_length=333, null=True,validators=[only_letters])
    empresa_referencia_1 = models.CharField("Empresa", max_length=333, null=True, blank=True,validators=[simple_text])
    tiempo_referencia_1 = models.IntegerField("Tiempo de Conocido (Años)", null=True,
                                              validators=[MinValueValidator(0), MaxValueValidator(333)])
    ciudad_referencia_1 = models.CharField("Ciudad", max_length=333, null=True,validators=[simple_text])
    telefono_referencia_1 = models.IntegerField("Teléfono", null=True,
                                                validators=[MinValueValidator(100000), MaxValueValidator(999_999_999_999)])
    tipo_via_referencia_1 = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_referencia_1 = models.CharField("Número", max_length=10, null=True, blank=True,validators=[only_numbers])
    letra_principal_referencia_1 = models.CharField("Letra", max_length=2, null=True, blank=True,
                                                    choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_referencia_1 = models.BooleanField("¿Bis?", default=False)
    letra_bis_referencia_1 = models.CharField("Letra Bis", max_length=2, blank=True, null=True,
                                              choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_referencia_1 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_referencia_1 = models.CharField("Número", max_length=10, null=True, blank=True,validators=[only_numbers])
    letra_secundaria_referencia_1 = models.CharField("Letra", max_length=2, blank=True, null=True,
                                                     choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_referencia_1 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_referencia_1 = models.CharField("Número Final", max_length=30, blank=True, null=True,validators=[only_numbers])
    complemento_referencia_1 = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True,validators=[simple_text])
    direccion_formateada_referencia_1 = models.CharField(max_length=500, blank=True, null=True,validators=[simple_text])

    # --- Referencia 2 ---
    nombre_referencia_2 = models.CharField("Nombres y apellidos", max_length=333, null=True,validators=[only_letters])
    ocupacion_referencia_2 = models.CharField("Ocupación", max_length=333, null=True,validators=[only_letters])
    empresa_referencia_2 = models.CharField("Empresa", max_length=333, null=True, blank=True,validators=[simple_text])
    tiempo_referencia_2 = models.IntegerField("Tiempo de Conocido (Años)", null=True,
                                              validators=[MinValueValidator(0), MaxValueValidator(333)])
    ciudad_referencia_2 = models.CharField("Ciudad", max_length=333, null=True,validators=[simple_text])
    telefono_referencia_2 = models.IntegerField("Teléfono", null=True,
                                                validators=[MinValueValidator(100000), MaxValueValidator(999_999_999_999)])
    tipo_via_referencia_2 = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_referencia_2 = models.CharField("Número", max_length=10, null=True, blank=True,validators=[only_numbers])
    letra_principal_referencia_2 = models.CharField("Letra", max_length=2, null=True, blank=True,
                                                    choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_referencia_2 = models.BooleanField("¿Bis?", default=False)
    letra_bis_referencia_2 = models.CharField("Letra Bis", max_length=2, blank=True, null=True,
                                              choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_referencia_2 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_referencia_2 = models.CharField("Número", max_length=10, null=True, blank=True,validators=[only_numbers])
    letra_secundaria_referencia_2 = models.CharField("Letra", max_length=2, blank=True, null=True,
                                                     choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_referencia_2 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_referencia_2 = models.CharField("Número Final", max_length=30, blank=True, null=True,validators=[only_numbers])
    complemento_referencia_2 = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True,validators=[simple_text])
    direccion_formateada_referencia_2 = models.CharField(max_length=500, blank=True, null=True,validators=[simple_text])

    # --- Referencia 3 ---
    nombre_referencia_3 = models.CharField("Nombres y apellidos", max_length=333, null=True,validators=[only_letters])
    ocupacion_referencia_3 = models.CharField("Ocupación", max_length=333, null=True,validators=[only_letters])
    empresa_referencia_3 = models.CharField("Empresa", max_length=333, null=True, blank=True,validators=[simple_text])
    tiempo_referencia_3 = models.IntegerField("Tiempo de Conocido (Años)", null=True,
                                              validators=[MinValueValidator(0), MaxValueValidator(333)])
    ciudad_referencia_3 = models.CharField("Ciudad", max_length=333, null=True,validators=[simple_text])
    telefono_referencia_3 = models.IntegerField("Teléfono", null=True,
                                                validators=[MinValueValidator(100000), MaxValueValidator(999_999_999_999)])
    tipo_via_referencia_3 = models.CharField("Tipo de vía", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Anillo Vial'), ('Autopista', 'Autopista'), ('Avenida', 'Avenida'),
        ('Avenida Calle', 'Avenida Calle'), ('Avenida Carrera', 'Avenida Carrera'), ('Calle', 'Calle'),
        ('Callejón', 'Callejón'), ('Carrera', 'Carrera'), ('Circular', 'Circular'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Transversal'),
    ])
    numero_principal_referencia_3 = models.CharField("Número", max_length=10, null=True, blank=True,validators=[only_numbers])
    letra_principal_referencia_3 = models.CharField("Letra", max_length=2, null=True, blank=True,
                                                    choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis_referencia_3 = models.BooleanField("¿Bis?", default=False)
    letra_bis_referencia_3 = models.CharField("Letra Bis", max_length=2, blank=True, null=True,
                                              choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_referencia_3 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    numero_secundario_referencia_3 = models.CharField("Número", max_length=10, null=True, blank=True,validators=[only_numbers])
    letra_secundaria_referencia_3 = models.CharField("Letra", max_length=2, blank=True, null=True,
                                                     choices=[(chr(c), chr(c)) for c in range(65, 91)])
    cuadrante_dos_referencia_3 = models.CharField("Cuadrante", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'ESTE'), ('OESTE', 'OESTE'), ('NORTE', 'NORTE'), ('SUR', 'SUR')
    ])
    nro_referencia_3 = models.CharField("Número Final", max_length=30, blank=True, null=True,validators=[only_numbers])
    complemento_referencia_3 = models.CharField("Complemento/Dirección especial", max_length=30, blank=True, null=True)
    direccion_formateada_referencia_3 = models.CharField(max_length=500, blank=True, null=True,validators=[simple_text])

    class Meta:
        verbose_name = "Referencias Personales"
        verbose_name_plural = "Referencias Personales"

    def __str__(self):
        """
        Retorna una representación legible del objeto en el panel de administración o consola.

        Returns:
            str: Texto identificador que incluye el ID de la instancia.
        """
        return f"Referencias Personales {self.id}"



class BienesRentasAEP(models.Model):
    
    """
    Modelo que representa la información financiera, patrimonial y económica
    del aspirante a través del formulario AEP (Autodeclaración Económica y Patrimonial).
    Incluye ingresos, cuentas bancarias, bienes patrimoniales, obligaciones financieras,
    participación en organizaciones y actividad económica privada.
    """

    # Relación con el aspirante
    PersonalData = models.ForeignKey('PersonalData', on_delete=models.CASCADE, related_name='bienes_rentas',null=True)
    salarios_y_demas_ingresos_laborales = models.IntegerField("Salarios y demás ingresos laborales", null=True, blank=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999)])
    cesantías_e_intereses_de_cesantías = models.IntegerField("Cesantías e intereses de cesantías", null=True, blank=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999)])
    gastos_de_representación = models.IntegerField("Gastos de representación", null=True, blank=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999)])
    arriendos = models.IntegerField("Arriendos", null=True, blank=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999)])
    honorarios = models.IntegerField("Honorarios", null=True, blank=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999)])
    otros_ingresos_y_rentas = models.IntegerField("Otros ingresos y rentas", null=True, blank=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999)])

    # Cuentas bancarias (nacionales e internacionales)

    entidad_financiera_1 = models.CharField("Entidad Financiera 1", blank=True,null=True,max_length=60,validators=[simple_text])
    tipo_de_cuenta_1 = models.CharField("Tipo de cuenta 1", blank=True,null=True,max_length=60,validators=[alphanumeric])
    numero_de_cuenta_1 = models.IntegerField("Numero de cuenta 1",blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])

    entidad_financiera_2 = models.CharField("Entidad Financiera 2", blank=True,null=True,max_length=60,validators=[simple_text])
    tipo_de_cuenta_2 = models.CharField("Tipo de cuenta 2", blank=True,null=True,max_length=60,validators=[alphanumeric])
    numero_de_cuenta_2 = models.IntegerField("Numero de cuenta 2",blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])



# Bienes patrimoniales
    
    tipo_bien_1 = models.CharField("Tipo de bien 1", blank=True,null=True,max_length=333,validators=[simple_text])
    ubicacion_bien_1 = models.CharField("Ubicación del bien 1 (Ciudad)",blank=True,null=True,max_length=333,validators=[simple_text])
    identificacion_bien_1 = models.CharField("Identificación del bien 1", blank=True,null=True, max_length=333,validators=[simple_text])
    avaluo_comercial_bien_1 = models.IntegerField("Avalúo comercial del bien 1",blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])

    tipo_bien_2 = models.CharField("Tipo de bien 2", blank=True,null=True,max_length=333,validators=[simple_text])
    ubicacion_bien_2 = models.CharField("Ubicación del bien 2 (Ciudad)",blank=True,null=True,max_length=333,validators=[simple_text])
    identificacion_bien_2 = models.CharField("Identificación del bien 2", blank=True,null=True, max_length=333,validators=[simple_text])
    avaluo_comercial_bien_2 = models.IntegerField("Avalúo comercial del bien 2",blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])



# Obligaciones financieras vigentes
    entidad_o_persona_obligacion_1 = models.CharField("Entidad o persona", blank=True, null=True,max_length=333,validators=[simple_text])
    concepto_obligacion_1 = models.CharField("Concepto", blank=True, null=True,max_length=333,validators=[simple_text])
    valor_1 = models.IntegerField("Valor" ,blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])

    entidad_o_persona_obligacion_2 = models.CharField("Entidad o persona", blank=True, null=True,max_length=333,validators=[simple_text])
    concepto_obligacion_2 = models.CharField("Concepto", blank=True, null=True,max_length=333,validators=[simple_text])
    valor_2 = models.IntegerField("Valor" ,blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(999_999_999_999_999)])



# Participación en entidades u organizaciones
    entidad_o_institucion_1 = models.CharField("Entidad o institución 1", blank=True,null=True,max_length=333,validators=[simple_text])
    calidad_de_miembro_1 = models.CharField("Calidad de miembro 1", blank=True,null=True,max_length=333,validators=[alphanumeric])
    entidad_o_institucion_2 = models.CharField("Entidad o institución 2", blank=True,null=True,max_length=333,validators=[simple_text])
    calidad_de_miembro_2 = models.CharField("Calidad de miembro 2", blank=True,null=True,max_length=333,validators=[alphanumeric])


# Actividad económica privada del aspirante
    empresa_1 = models.CharField("Empresa 1",blank=True,null=True,max_length=333,validators=[simple_text])
    calidad_de_miembro_AEP_1 = models.CharField("Calidad de miembro 1",blank=True,null=True,max_length=333,validators=[alphanumeric])
    empresa_2 = models.CharField("Empresa 2",blank=True,null=True,max_length=333,validators=[simple_text])
    calidad_de_miembro_AEP_2 = models.CharField("Calidad de miembro 2",blank=True,null=True,max_length=333,validators=[alphanumeric])


    class Meta:
        verbose_name = "Bienes y Rentas AEP"
        verbose_name_plural = "Bienes y Rentas AEP"

    def __str__(self):
        return f"Bienes y Rentas AEP {self.id}"


class SituacionJuridica(models.Model):

    """
    Modelo que almacena información sobre procesos judiciales, disciplinarios o
    administrativos asociados al aspirante. Permite registrar hasta dos procesos
    diferentes con detalles como tipo de investigación, autoridad competente,
    estado y responsabilidad.
    """

    PersonalData = models.ForeignKey('PersonalData', on_delete=models.CASCADE, related_name='situaciones_juridicas',null=True)
 # Primer proceso
    fecha_proceso_1 = models.DateField("Fecha Proceso 1", blank=True, null=True)
    tipo_de_investigacion_1 = models.CharField("Tipo de Investigación 1", blank=True,null=True,max_length=333,validators=[simple_text])
    causa_1 = models.CharField("Causa 1", blank=True,null=True,max_length=333,validators=[simple_text])
    autoridad_1 = models.CharField("Autoridad 1", blank=True,null=True,max_length=333,validators=[simple_text])
    estado_del_proceso_1 = models.CharField("Estado del Proceso 1", blank=True,null=True,max_length=333,validators=[simple_text])
    responsable_1 = models.CharField("¿Responsable?", blank=True,null=True,max_length=333,choices=[("Sí","Sí"),("No","No")])

# Segundo proceso
    fecha_proceso_2 = models.DateField("Fecha Proceso 2", blank=True, null=True,validators=[simple_text])
    tipo_de_investigacion_2 = models.CharField("Tipo de Investigación 2", blank=True,null=True,max_length=333,validators=[simple_text])
    causa_2 =  models.CharField("Causa 2", blank=True,null=True,max_length=333,validators=[simple_text])
    autoridad_2 = models.CharField("Autoridad 2", blank=True,null=True,max_length=333,validators=[simple_text])
    estado_del_proceso_2 = models.CharField("Estado del Proceso 2", blank=True,null=True,max_length=333,validators=[simple_text])
    responsable_2 = models.CharField("¿Responsable?", blank=True,null=True,max_length=333,choices=[("Sí","Sí"),("No","No")])
    
    def __str__(self):
        return f"Situación Jurídica {self.id}"




class DocumentoGenerado(models.Model):
    PersonalData = models.ForeignKey(PersonalData, on_delete=models.CASCADE, related_name="documentos")
    tipo = models.CharField(max_length=50)
    archivo = models.FileField(upload_to="documentos/%Y/%m/")
    

    def __str__(self):
        return f"{self.tipo} de {self.PersonalData}"

