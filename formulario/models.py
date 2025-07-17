
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator

# --- Validadores REGEX ---

only_letters = RegexValidator(r'^[A-Za-zÁÉÍÓÚÑáéíóúñ ]+$', 'Only letters and spaces are allowed.')
alphanumeric = RegexValidator(r'^[A-Za-zÁÉÍÓÚÑáéíóúñ0-9 ]+$', 'Only letters, numbers, and spaces are allowed.')
simple_text = RegexValidator(r'^[A-Za-zÁÉÍÓÚÑÜüöÖäÄáéíóúñ0-9\s.,¨:#-]*$', 'Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.')
only_numbers = RegexValidator(r'^\d+$', 'Only numbers are allowed.')

class PersonalData(models.Model):
    """
    Model representing personal, identification, and contact information
    of a person registered as a recruit in the system.

    It includes multiple fields such as full name, ID documents,
    birth information, military card, physical traits, detailed address,
    and social networks. Key fields are validated to ensure data integrity
    and uniqueness.
    """

    # --- Personal Information ---
    first_name = models.CharField("First name", max_length=30, validators=[only_letters])
    second_name = models.CharField("Second name", max_length=30, blank=True, validators=[only_letters])
    lastname = models.CharField("Last name", max_length=80, validators=[only_letters])
    second_lastname = models.CharField("Second last name", max_length=80, blank=True, validators=[only_letters])

    # --- Identity Documents ---
    document_type = models.CharField("Document type", max_length=2, choices=[("CC", "Citizen ID"), ("CE", "Foreigner ID")])
    document_number = models.IntegerField("Document number", unique=True, validators=[MinValueValidator(1_000), MaxValueValidator(99_999_999_999)])
    expedition_date = models.DateField("ID issue date")
    expedition_place = models.CharField("ID issue place", max_length=20, validators=[only_letters])
    passport_number = models.CharField("Passport number", max_length=12, blank=True, validators=[alphanumeric])
    passport_date = models.DateField("Passport issue date", null=True, blank=True)

    # --- Birth Date (distributed) ---
    birth_day = models.IntegerField("Day of birth", null=True, choices=[(i, str(i)) for i in range(1, 32)])
    birth_month = models.CharField(
        "Month of birth", max_length=13, null=True,
        choices=[(str(i), month) for i, month in enumerate([
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ], start=1)]
    )
    birth_year = models.IntegerField("Year of birth", null=True, validators=[MinValueValidator(1900), MaxValueValidator(2025)])

    # --- Marital Status and Profession ---
    relationships = models.CharField("Marital status", max_length=30, null=True, choices=[
        ("Married", "Married"), ("Single", "Single"),
    ("Common-law marriage", "Common-law marriage"),
    ("Separated", "Separated"), ("Divorced", "Divorced"), ("Widowed", "Widowed")
    ])
    profession = models.CharField("Profession or occupation", max_length=30, null=True, validators=[only_letters])
    profesional_id = models.CharField("Professional ID card", max_length=15, null=True, validators=[alphanumeric])
    body_marks = models.CharField("Body marks", max_length=50, null=True, validators=[simple_text])
    height = models.IntegerField("Height (cm)", null=True, validators=[MinValueValidator(80), MaxValueValidator(400)])
    weight = models.IntegerField("Weight (kg)", null=True, validators=[MinValueValidator(10), MaxValueValidator(500)])

    # --- Address (structured) ---
    street_type = models.CharField("Street type", max_length=20, null=True, choices=[
        ('Anillo Vial', 'Ring road'), ('Autopista', 'Highway'),
        ('Avenida', 'Avenue'), ('Avenida Calle', 'Avenue Street'),
        ('Avenida Carrera', 'Avenue Road'), ('Calle', 'Street'),
        ('Callejón', 'Alley'), ('Carrera', 'Road'),
        ('Circular', 'Circle'), ('Diagonal', 'Diagonal'),
        ('Transversal', 'Cross street')
    ])
    principal_number = models.CharField("Main number", max_length=10, null=True, validators=[only_numbers])
    principal_letter = models.CharField("Main letter", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    bis = models.BooleanField("Bis?", default=False)
    bis_letter = models.CharField("Bis letter", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    quadrant = models.CharField("Quadrant", max_length=10, choices=[
        ('ESTE', 'EAST'), ('OESTE', 'WEST'), ('NORTE', 'NORTH'), ('SUR', 'SOUTH')
    ], blank=True, null=True)
    secondary_number = models.CharField("Secondary number", max_length=10, null=True, validators=[only_numbers])
    secondary_letter = models.CharField("Secondary letter", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    quadrant_2 = models.CharField("Second quadrant", max_length=10, choices=[
        ('ESTE', 'EAST'), ('OESTE', 'WEST'), ('NORTE', 'NORTH'), ('SUR', 'SOUTH')
    ], blank=True, null=True)
    nmbr = models.CharField("Final number", max_length=30, blank=True, null=True, validators=[only_numbers])
    complement = models.CharField("Address complement / special location", max_length=30, blank=True, null=True, validators=[simple_text])
    neighborhood = models.CharField("Neighborhood", max_length=50, null=True, validators=[alphanumeric])

    # --- Contact ---
    phone_number = models.IntegerField("Mobile phone number", unique=True, null=True, validators=[MinValueValidator(1_000), MaxValueValidator(99_999_999_999)])
    landline_phone = models.IntegerField("Landline phone number", blank=True, null=True, validators=[MinValueValidator(1_000), MaxValueValidator(99_999_999_999)])
    city = models.CharField("City of birth", max_length=30, null=True, validators=[only_letters])
    department = models.CharField("Department of birth", max_length=30, null=True, validators=[only_letters])
    personal_email = models.EmailField("Personal email address", null=True)

    # Automatically generated address
    formated_address = models.CharField("Formatted address", max_length=500, blank=True, null=True, validators=[simple_text])

    class Meta:
        verbose_name = "PersonalData"
        verbose_name_plural = "PersonalData"

    @property
    def nombres(self):
        """
        Returns the concatenated first and second names, avoiding extra spaces.
        """
        return f"{self.first_name} {self.second_name}".strip()

    @property
    def apellidos(self):
        """
        Returns the concatenated last names, avoiding extra spaces.
        """
        return f"{self.lastname} {self.second_lastname}".strip()

    @property
    def direccion_completa(self):
        """
        Builds and returns the recruit's complete address in a structured format.
        """
        parts = [
            self.street_type,
            self.principal_number,
            self.principal_letter,
            "BIS" if self.bis else "",
            self.bis_letter,
            self.quadrant,
        ]
        if self.secondary_number:
            parts.extend(["#", self.secondary_number, self.secondary_letter, self.quadrant_2])
        parts.append(self.nmbr)
        address = " ".join(filter(None, parts))
        if self.complement:
            address += f", {self.complement}"
        return address.strip()

    def save(self, *args, **kwargs):
        """
        Automatically generates and saves the formatted address upon saving the object.
        """
        self.formated_address = self.direccion_completa
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a readable representation of the object (full name).
        """
        return f"{self.nombres} {self.apellidos}"



class FamilyData(models.Model):
    """
    Model that stores detailed family information of the recruit.

    Includes spouse, father, and mother data such as names, IDs, phones,
    professions, and addresses. The address fields follow the same structure
    used in the main PersonalData model.

    Has a 1:1 relationship with a single PersonalData object.

    Attributes:
        PersonalData (OneToOneField): Direct relationship with the PersonalData model.
        spouse_name (CharField): Full name of the spouse.
        spouse_id (CharField): Spouse's ID.
        ... (similar attributes for father and mother)
    """

    # One-to-one relationship with PersonalData
    PersonalData = models.OneToOneField(PersonalData, on_delete=models.CASCADE, null=True)

    # --- Spouse data ---
    spouse_name = models.CharField("Spouse's Name", max_length=50, blank=True, validators=[only_letters])
    spouse_id = models.IntegerField("Spouse's ID", validators=[MinValueValidator(1_000), MaxValueValidator(999_999_999_999)], blank=True, null=True)
    spouse_profession = models.CharField("Spouse's Profession", max_length=50, blank=True, null=True, validators=[only_letters])
    spouse_phone = models.IntegerField("Spouse's Mobile", max_length=15, blank=True, validators=[MinValueValidator(1_000), MaxValueValidator(999_999_999_999)])
    spouse_street_type = models.CharField("Street Type", max_length=20, null=True, blank=True, choices=[
    ('Ring Road', 'Ring Road'), ('Highway', 'Highway'), ('Avenue', 'Avenue'),
    ('Avenue Street', 'Avenue Street'), ('Avenue Road', 'Avenue Road'), ('Street', 'Street'),
    ('Alley', 'Alley'), ('Road', 'Road'), ('Circle', 'Circle'),
    ('Diagonal', 'Diagonal'), ('Cross Street', 'Cross Street'),
    ])
    spouse_principal_number = models.CharField("Main Number", max_length=10, null=True, blank=True, validators=[only_numbers])
    spouse_principal_letter = models.CharField("Main Letter", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    spouse_bis = models.BooleanField("Bis?", default=False)
    spouse_bis_letter = models.CharField("Bis Letter", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    spouse_quadrant = models.CharField("Quadrant", max_length=10, blank=True, null=True, choices=[
       ('EAST', 'EAST'), ('WEST', 'WEST'), ('NORTH', 'NORTH'), ('SOUTH', 'SOUTH')
    ])
    spouse_second_number = models.CharField("Secondary Number", max_length=10, null=True, blank=True, validators=[only_numbers])
    spouse_second_letter = models.CharField("Secondary Letter", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    spouse_second_quadrant = models.CharField("Secondary Quadrant", max_length=10, blank=True, null=True, choices=[
        ('EAST', 'EAST'), ('WEST', 'WEST'), ('NORTH', 'NORTH'), ('SOUTH', 'SOUTH')
    ])
    spouse_nmbr = models.CharField("Final Number", max_length=30, blank=True, null=True, validators=[only_numbers])
    spouse_complement = models.CharField("Complement/Special Address", max_length=30, blank=True, null=True, validators=[simple_text])
    spouse_built_address = models.CharField("Formatted Address", max_length=500, blank=True, null=True, validators=[simple_text])

    # --- Father data ---
    father_name = models.CharField("Father's Name", max_length=55, null=True, validators=[only_letters])
    father_lives = models.CharField("Is Alive?", null=True, choices=[("Yes", "Yes"), ("No", "No")])
    father_id = models.IntegerField("ID No.", null=True, validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    father_phone = models.IntegerField("Father's Phone", blank=True, null=True, validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    father_profession = models.CharField("Father's Profession", blank=True, null=True, max_length=50, validators=[only_letters])

    father_street_type = models.CharField("Street Type", max_length=20, null=True, blank=True, choices=[
    ('Ring Road', 'Ring Road'), ('Highway', 'Highway'), ('Avenue', 'Avenue'),
    ('Avenue Street', 'Avenue Street'), ('Avenue Road', 'Avenue Road'), ('Street', 'Street'),
    ('Alley', 'Alley'), ('Road', 'Road'), ('Circle', 'Circle'),
    ('Diagonal', 'Diagonal'), ('Cross Street', 'Cross Street'),
    ])
    father_principal_number = models.CharField("Main Number", max_length=10, null=True, blank=True, validators=[only_numbers])
    father_principal_letter = models.CharField("Main Letter", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    father_bis = models.BooleanField("Bis?", default=False)
    father_bis_letter = models.CharField("Bis Letter", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    father_quadrant = models.CharField("Quadrant", max_length=10, blank=True, null=True, choices=[
       ('EAST', 'EAST'), ('WEST', 'WEST'), ('NORTH', 'NORTH'), ('SOUTH', 'SOUTH')
    ])
    father_second_number = models.CharField("Secondary Number", max_length=10, null=True, blank=True, validators=[only_numbers])
    father_second_letter = models.CharField("Secondary Letter", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    father_second_quadrant = models.CharField("Secondary Quadrant", max_length=10, blank=True, null=True, choices=[
       ('EAST', 'EAST'), ('WEST', 'WEST'), ('NORTH', 'NORTH'), ('SOUTH', 'SOUTH')
    ])
    father_nmbr = models.CharField("Final Number", max_length=30, blank=True, null=True, validators=[only_numbers])
    father_complement = models.CharField("Complement/Special Address", max_length=30, blank=True, null=True, validators=[simple_text])
    father_built_address = models.CharField("Formatted Address", max_length=500, blank=True, null=True, validators=[simple_text])

    # --- Mother data ---
    mother_name = models.CharField("Mother's Name", max_length=55, null=True, validators=[only_letters])
    mother_lives = models.CharField("Is Alive?", null=True, choices=[("Sí", "Yes"), ("No", "No")])
    mother_id = models.IntegerField("ID No.", null=True, validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    mother_phone = models.IntegerField("Mother's Phone", blank=True, null=True, validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)])
    mother_profession = models.CharField("Mother's Profession", blank=True, null=True, max_length=50, validators=[only_letters])

    mother_street_type = models.CharField("Street Type", max_length=20, null=True, blank=True, choices=[
    ('Ring Road', 'Ring Road'), ('Highway', 'Highway'), ('Avenue', 'Avenue'),
    ('Avenue Street', 'Avenue Street'), ('Avenue Road', 'Avenue Road'), ('Street', 'Street'),
    ('Alley', 'Alley'), ('Road', 'Road'), ('Circle', 'Circle'),
    ('Diagonal', 'Diagonal'), ('Cross Street', 'Cross Street'),
    ])
    mother_principal_number = models.CharField("Main Number", max_length=10, null=True, blank=True, validators=[only_numbers])
    mother_principal_letter = models.CharField("Main Letter", max_length=2, null=True, blank=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    mother_bis = models.BooleanField("Bis?", default=False)
    mother_bis_letter = models.CharField("Bis Letter", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    mother_quadrant = models.CharField("Quadrant", max_length=10, blank=True, null=True, choices=[
         ('EAST', 'EAST'), ('WEST', 'WEST'), ('NORTH', 'NORTH'), ('SOUTH', 'SOUTH')
    ])
    mother_second_number = models.CharField("Secondary Number", max_length=10, null=True, blank=True, validators=[only_numbers])
    mother_second_letter = models.CharField("Secondary Letter", max_length=2, blank=True, null=True, choices=[(chr(c), chr(c)) for c in range(65, 91)])
    mother_second_quadrant = models.CharField("Secondary Quadrant", max_length=10, blank=True, null=True, choices=[
         ('EAST', 'EAST'), ('WEST', 'WEST'), ('NORTH', 'NORTH'), ('SOUTH', 'SOUTH')
    ])
    mother_nmbr = models.CharField("Final Number", max_length=30, blank=True, null=True, validators=[only_numbers])
    mother_complement = models.CharField("Complement/Special Address", max_length=30, blank=True, null=True, validators=[simple_text])
    mother_built_address = models.CharField("Formatted Address", max_length=500, blank=True, null=True, validators=[simple_text])

    class Meta:
        verbose_name = "Family Data"
        verbose_name_plural = "Family Data"

    def __str__(self):
        """
        Returns a readable representation of the object.

        Returns:
            str: Identifier text with the object ID.
        """
        return f"Family Data {self.id}"

    @property
    def spouse_full_address(self):
        """
        Builds the complete address of the spouse from the structured fields.

        Returns:
            str: Formatted address of the spouse.
        """
        parts = [
            self.spouse_street_type,
            self.spouse_principal_number,
            self.spouse_principal_letter,
            "BIS" if self.spouse_bis else "",
            self.spouse_bis_letter,
            self.spouse_quadrant,
        ]
        if self.spouse_second_number:
            parts.extend([
                "#", self.spouse_second_number,
                self.spouse_second_letter, self.spouse_second_quadrant
            ])
        parts.append(self.spouse_nmbr)
        address = " ".join(filter(None, parts))
        if self.spouse_complement:
            address += f", {self.spouse_complement}"
        return address.strip()

    def save(self, *args, **kwargs):
        """
        When saving the object, generates and saves the formatted spouse address.
        """
        self.spouse_built_address = self.spouse_full_address
        super().save(*args, **kwargs)


class Child(models.Model):
    """
    Model representing a child of the applicant, linked through FamilyData.

    Each child is associated with a FamilyData instance and includes their
    name, age, and identification number.

    Attributes:
        FamilyData (ForeignKey): Many-to-one relationship with `FamilyData`.
        name (CharField): Child's full name.
        age (IntegerField): Child's age, validated to be between 0 and 200 years.
        id (IntegerField): Child's ID number.
    """

    FamilyData = models.ForeignKey(
        'FamilyData',
        on_delete=models.CASCADE,
        related_name="children"
    )

    name = models.CharField("Child's name", max_length=50, validators=[only_letters])
    age = models.IntegerField("Age", validators=[MinValueValidator(0), MaxValueValidator(200)])
    child_id = models.IntegerField("Identification number", validators=[MinValueValidator(0), MaxValueValidator(99999_999_999)])

    def __str__(self):
        """
        Returns a readable representation of the child, including name and age.

        Returns:
            str: Formatted name and age for display.
        """
        return f"{self.name} ({self.age} years old)"


class Sibling(models.Model):
    """
    Model representing a sibling of the applicant.

    Each sibling is linked to a `FamilyData` instance and contains personal,
    contact, and structured address data similar to the applicant.

    Attributes:
        FamilyData (ForeignKey): Link to `FamilyData` model.
        sibling_lastname (CharField): Sibling's last name.
        sibling_second_lastname (CharField): Sibling's second last name.
        sibling_first_name (CharField): Sibling's first name.
        sibling_second_name (CharField): Sibling's middle name.
        sibling_id (IntegerField): Identification number.
        sibling_occupation (CharField): Current profession or occupation.
        sibling_phone (IntegerField): Contact phone number.
        ...structured address fields...
    """

    FamilyData = models.ForeignKey(
        'FamilyData',
        on_delete=models.CASCADE,
        related_name="siblings"
    )

    # Personal and contact information
    sibling_lastname = models.CharField("Last name", blank=True, null=True, max_length=30, validators=[only_letters])
    sibling_second_lastname = models.CharField("Second last name", blank=True, null=True, max_length=30, validators=[only_letters])
    sibling_first_name = models.CharField("First name", blank=True, null=True, max_length=30, validators=[only_letters])
    sibling_second_name = models.CharField("Middle name", blank=True, null=True, max_length=30, validators=[only_letters])
    sibling_id = models.IntegerField(
        "ID number",
        blank=True, null=True,
        validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)]
    )
    sibling_occupation = models.CharField("Occupation", blank=True, null=True, max_length=60, validators=[only_letters])
    sibling_phone = models.IntegerField(
        "Phone number",
        blank=True, null=True,
        validators=[MinValueValidator(100), MaxValueValidator(99_999_999_999)]
    )

    # Structured address
    sibling_street_type = models.CharField("Street type", max_length=20, null=True, blank=True, choices=[
        ('Anillo Vial', 'Ring road'), ('Autopista', 'Highway'), ('Avenida', 'Avenue'),
        ('Avenida Calle', 'Avenue Street'), ('Avenida Carrera', 'Avenue Avenue'), ('Calle', 'Street'),
        ('Callejón', 'Alley'), ('Carrera', 'Avenue'), ('Circular', 'Circle'),
        ('Diagonal', 'Diagonal'), ('Transversal', 'Cross street')
    ])
    sibling_principal_number = models.CharField("Main number", max_length=10, null=True, blank=True, validators=[only_numbers])
    sibling_principal_letter = models.CharField("Main letter", max_length=2, null=True, blank=True, choices=[
        (chr(c), chr(c)) for c in range(65, 91)
    ])
    sibling_bis = models.BooleanField("Bis?", default=False)
    sibling_bis_letter = models.CharField("Bis letter", max_length=2, blank=True, null=True, choices=[
        (chr(c), chr(c)) for c in range(65, 91)
    ])
    sibling_quadrant = models.CharField("Quadrant", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'EAST'), ('OESTE', 'WEST'), ('NORTE', 'NORTH'), ('SUR', 'SOUTH')
    ])
    sibling_second_number = models.CharField("Secondary number", max_length=10, null=True, blank=True, validators=[only_numbers])
    sibling_second_letter = models.CharField("Secondary letter", max_length=2, blank=True, null=True, choices=[
        (chr(c), chr(c)) for c in range(65, 91)
    ])
    sibling_second_quadrant = models.CharField("Second quadrant", max_length=10, blank=True, null=True, choices=[
        ('ESTE', 'EAST'), ('OESTE', 'WEST'), ('NORTE', 'NORTH'), ('SUR', 'SOUTH')
    ])
    sibling_nmbr = models.CharField("Final number", max_length=30, blank=True, null=True, validators=[only_numbers])
    sibling_complement = models.CharField("Address complement / special location", max_length=30, blank=True, null=True, validators=[simple_text])
    sibling_built_address = models.CharField("Formatted address", max_length=500, blank=True, null=True, validators=[simple_text])

    def __str__(self):
        """
        Returns a readable string representation of the sibling for admin or shell.

        Returns:
            str: Sibling's name and ID in compact format.
        """
        return f"{self.sibling_first_name or ''} {self.sibling_lastname or ''} - {self.sibling_id or ''}".strip()

class AcademicInformation(models.Model):
    """
    Model that stores academic background and knowledge in foreign languages and office tools.

    Includes up to two levels of formal education, two foreign languages with assessed skills
    (reading, writing, speaking), and knowledge of common office tools such as Word, Excel, etc.

    Attributes:
        PersonalData (ForeignKey): Link to the `PersonalData` model.
        studies_X (CharField): Description of completed studies at each level.
        studies_X_year (IntegerField): Year of completion.
        studies_title_X (CharField): Degree obtained.
        studies_institution_name_X (CharField): Name of the educational institution.
        studies_city_X (CharField): City where the studies took place.
        foreign_language_X (CharField): Declared foreign language.
        can_read_ / can_speak_ / can_write_ (CharField): Assessed language skills.
        word_check / excel_check / ... (CharField): Knowledge in office tools.
        other_check (CharField): Free field for declaring additional tools.
    """

    PersonalData = models.ForeignKey(
        'PersonalData',
        on_delete=models.CASCADE,
        related_name='academic_information',
        null=True
    )

    # --- Formal Education (up to 2 records) ---
    studies_1 = models.CharField("Completed Studies 1", max_length=50, blank=True, null=True, validators=[only_letters])
    studies_1_year = models.IntegerField("Year", blank=True, null=True,
                                         validators=[MinValueValidator(1900), MaxValueValidator(2030)])
    studies_title_1 = models.CharField("Degree Obtained", max_length=50, blank=True, null=True, validators=[simple_text])
    studies_institution_name_1 = models.CharField("Institution Name", max_length=70, blank=True, null=True, validators=[simple_text])
    studies_city_1 = models.CharField("City", max_length=50, blank=True, null=True, validators=[simple_text])

    studies_2 = models.CharField("Completed Studies 2", max_length=50, blank=True, null=True, validators=[simple_text])
    studies_2_year = models.IntegerField("Year", blank=True, null=True,
                                         validators=[MinValueValidator(1900), MaxValueValidator(2030)])
    studies_title_2 = models.CharField("Degree Obtained", max_length=50, blank=True, null=True, validators=[simple_text])
    studies_institution_name_2 = models.CharField("Institution Name", max_length=70, blank=True, null=True, validators=[simple_text])
    studies_city_2 = models.CharField("City", max_length=50, blank=True, null=True, validators=[simple_text])

    # --- Foreign Languages (up to 2) ---
    foreign_language_1 = models.CharField("Foreign Language 1", max_length=50, blank=True, null=True, validators=[simple_text])
    can_read_foreign_language_1 = models.CharField("Can Read?", null=True, blank=True, choices=[("Yes", "Yes"), ("No", "No")])
    can_speak_foreign_language_1 = models.CharField("Can Speak?", null=True, blank=True, choices=[("Yes", "Yes"), ("No", "No")])
    can_write_foreign_language_1 = models.CharField("Can Write?", null=True, blank=True, choices=[("Yes", "Yes"), ("No", "No")])

    foreign_language_2 = models.CharField("Foreign Language 2", max_length=50, blank=True, null=True, validators=[simple_text])
    can_read_foreign_language_2 = models.CharField("Can Read?", null=True, blank=True, choices=[("Yes", "Yes"), ("No", "No")])
    can_speak_foreign_language_2 = models.CharField("Can Speak?", null=True, blank=True, choices=[("Yes", "Yes"), ("No", "No")])
    can_write_foreign_language_2 = models.CharField("Can Write?", null=True, blank=True, choices=[("Yes", "Yes"), ("No", "No")])

    # --- Office Tools Knowledge ---
    word_check = models.CharField("Word", null=True, choices=[("Yes", "Yes"), ("No", "No")])
    excel_check = models.CharField("Excel", null=True, choices=[("Yes", "Yes"), ("No", "No")])
    powerpoint_check = models.CharField("PowerPoint", null=True, choices=[("Yes", "Yes"), ("No", "No")])
    access_check = models.CharField("Access", null=True, choices=[("Yes", "Yes"), ("No", "No")])
    internet_check = models.CharField("Internet", null=True, choices=[("Yes", "Yes"), ("No", "No")])
    other_check = models.CharField("Other Tools (comma-separated)", null=True, blank=True, max_length=333, validators=[simple_text])

    class Meta:
        verbose_name = "Academic Information"
        verbose_name_plural = "Academic Information Entries"

    def __str__(self):
        """
        Returns a string representation of the instance for admin or console.

        Returns:
            str: Identifier text with the ID of the academic information.
        """
        return f"Academic Information {self.id}"


class AssetsIncomeAEP(models.Model):
    """
    Model representing the financial, asset-related, and economic information
    of the applicant through the AEP form (Economic and Asset Self-Declaration).
    Includes income, bank accounts, assets, financial obligations,
    participation in organizations, and private economic activity.
    """

    # Relationship with the applicant
    PersonalData = models.ForeignKey('PersonalData', on_delete=models.CASCADE, related_name='AssetsIncomeAEP', null=True)

    salary_and_other_income = models.IntegerField("Salaries and other labor income", null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(999_999_999_999)])
    layoff_and_interests = models.IntegerField("Severance pay and interests", null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(999_999_999_999)])
    representation_expenses = models.IntegerField("Representation expenses", null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(999_999_999_999)])
    leases = models.IntegerField("Rentals", null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(999_999_999_999)])
    fee = models.IntegerField("Professional fees", null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(999_999_999_999)])
    other_income = models.IntegerField("Other income and earnings", null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(999_999_999_999)])

    # Bank accounts (domestic and international)
    financial_entity_1 = models.CharField("Financial Institution 1", blank=True, null=True, max_length=60, validators=[simple_text])
    account_type_1 = models.CharField("Account Type 1", blank=True, null=True, max_length=60, validators=[alphanumeric])
    account_number_1 = models.IntegerField("Account Number 1", blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(999_999_999_999_999)])

    financial_entity_2 = models.CharField("Financial Institution 2", blank=True, null=True, max_length=60, validators=[simple_text])
    account_type_2 = models.CharField("Account Type 2", blank=True, null=True, max_length=60, validators=[alphanumeric])
    account_number_2 = models.IntegerField("Account Number 2", blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(999_999_999_999_999)])

    # Assets
    good_type_1 = models.CharField("Type of Asset 1", blank=True, null=True, max_length=333, validators=[simple_text])
    good_location_1 = models.CharField("Asset Location 1 (City)", blank=True, null=True, max_length=333, validators=[simple_text])
    good_id_1 = models.CharField("Asset Identification 1", blank=True, null=True, max_length=333, validators=[simple_text])
    good_appraisal_1 = models.IntegerField("Commercial Appraisal of Asset 1", blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(999_999_999_999_999)])

    good_type_2 = models.CharField("Type of Asset 2", blank=True, null=True, max_length=333, validators=[simple_text])
    good_location_2 = models.CharField("Asset Location 2 (City)", blank=True, null=True, max_length=333, validators=[simple_text])
    good_id_2 = models.CharField("Asset Identification 2", blank=True, null=True, max_length=333, validators=[simple_text])
    good_appraisal_2 = models.IntegerField("Commercial Appraisal of Asset 2", blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(999_999_999_999_999)])

    # Current financial obligations
    obligation_entity_person_1 = models.CharField("Entity or Person 1", blank=True, null=True, max_length=333, validators=[simple_text])
    obligation_concept_1 = models.CharField("Concept 1", blank=True, null=True, max_length=333, validators=[simple_text])
    value_1 = models.IntegerField("Amount 1", blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(999_999_999_999_999)])

    obligation_entity_person_2 = models.CharField("Entity or Person 2", blank=True, null=True, max_length=333, validators=[simple_text])
    obligation_concept_2 = models.CharField("Concept 2", blank=True, null=True, max_length=333, validators=[simple_text])
    value_2 = models.IntegerField("Amount 2", blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(999_999_999_999_999)])

    # Participation in entities or organizations
    entity_or_institution_1 = models.CharField("Entity or Institution 1", blank=True, null=True, max_length=333, validators=[simple_text])
    kind_of_member_1 = models.CharField("Member Role 1", blank=True, null=True, max_length=333, validators=[alphanumeric])
    entity_or_institution_2 = models.CharField("Entity or Institution 2", blank=True, null=True, max_length=333, validators=[simple_text])
    kind_of_member_2 = models.CharField("Member Role 2", blank=True, null=True, max_length=333, validators=[alphanumeric])

    # Applicant's private economic activity
    company_1 = models.CharField("Company 1", blank=True, null=True, max_length=333, validators=[simple_text])
    kind_of_member_AEP_1 = models.CharField("Member Role 1", blank=True, null=True, max_length=333, validators=[alphanumeric])
    company_2 = models.CharField("Company 2", blank=True, null=True, max_length=333, validators=[simple_text])
    kind_of_member_AEP_2 = models.CharField("Member Role 2", blank=True, null=True, max_length=333, validators=[alphanumeric])

    class Meta:
        verbose_name = "AEP Assets and Income"
        verbose_name_plural = "AEP Assets and Income"

    def __str__(self):
        return f"AEP Assets and Income {self.id}"


class LegalSituation(models.Model):
    """
    Model that stores information about judicial, disciplinary, or
    administrative proceedings associated with the applicant. It allows recording
    up to two different cases with details such as type of investigation,
    competent authority, status, and responsibility.
    """

    PersonalData = models.ForeignKey(
        'PersonalData',
        on_delete=models.CASCADE,
        related_name='legal_situations',
        null=True
    )

    # First proceeding
    process_date_1 = models.DateField("Process Date 1", blank=True, null=True)
    investigation_type_1 = models.CharField("Investigation Type 1", blank=True, null=True, max_length=333, validators=[simple_text])
    cause_1 = models.CharField("Cause 1", blank=True, null=True, max_length=333, validators=[simple_text])
    autority_1 = models.CharField("Authority 1", blank=True, null=True, max_length=333, validators=[simple_text])
    process_state_1 = models.CharField("Process Status 1", blank=True, null=True, max_length=333, validators=[simple_text])
    responsible_1 = models.CharField("Responsible?", blank=True, null=True, max_length=333, choices=[("Yes", "Yes"), ("No", "No")])

    # Second proceeding
    process_date_2 = models.DateField("Process Date 2", blank=True, null=True)
    investigation_type_2 = models.CharField("Investigation Type 2", blank=True, null=True, max_length=333, validators=[simple_text])
    cause_2 = models.CharField("Cause 2", blank=True, null=True, max_length=333, validators=[simple_text])
    autority_2 = models.CharField("Authority 2", blank=True, null=True, max_length=333, validators=[simple_text])
    process_state_2 = models.CharField("Process Status 2", blank=True, null=True, max_length=333, validators=[simple_text])
    responsible_2 = models.CharField("Responsible?", blank=True, null=True, max_length=333, choices=[("Yes", "Yes"), ("No", "No")])

    def __str__(self):
        return f"Legal Situation {self.id}"




class DocumentoGenerado(models.Model):
    PersonalData = models.ForeignKey(PersonalData, on_delete=models.CASCADE, related_name="documentos")
    tipo = models.CharField(max_length=50)
    archivo = models.FileField(upload_to="documentos/%Y/%m/")
    

    def __str__(self):
        return f"{self.tipo} of {self.PersonalData}"

