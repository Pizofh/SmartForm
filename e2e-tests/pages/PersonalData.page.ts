import { Page, Locator } from '@playwright/test';

export class PersonalDataPage {
  readonly page: Page;
  readonly tab: Locator;

  readonly first_name: Locator;
  readonly second_name: Locator;
  readonly lastname: Locator;
  readonly second_lastname: Locator;
  readonly document_type: Locator;
  readonly document_number: Locator
  readonly expedition_date: Locator;
  readonly expedition_place: Locator;
  readonly passport_number: Locator;
  readonly passport_date: Locator;
  readonly birth_day: Locator;
  readonly birth_month: Locator;
  readonly birth_year: Locator;
  readonly relationships: Locator;
  readonly profession: Locator;
  readonly profesional_id: Locator;
  readonly body_marks: Locator;
  readonly height: Locator; 
  readonly weight: Locator; 
  readonly street_type: Locator; 
  readonly principal_number: Locator; 
  readonly principal_letter: Locator; 
  readonly bis: Locator; 
  readonly bis_letter: Locator; 
  readonly quadrant: Locator; 
  readonly secondary_number: Locator;
  readonly secondary_letter: Locator; 
  readonly quadrant_2: Locator;
  readonly nmbr: Locator; 
  readonly complement: Locator; 
  readonly neighborhood: Locator; 
  readonly phone_number: Locator;
  readonly landline_phone: Locator; 
  readonly city: Locator;
  readonly department: Locator; 
  readonly personal_email: Locator; 
  readonly formated_address: Locator; 


constructor(page: Page) {
  this.page = page;
  this.tab = page.locator('text=Personal Information');

  this.first_name = page.locator('#id_PersonalData-first_name');
  this.second_name = page.locator('#id_PersonalData-second_name');
  this.lastname = page.locator('#id_PersonalData-lastname');
  this.second_lastname = page.locator('#id_PersonalData-second_lastname');
  this.document_type = page.locator('#id_PersonalData-document_type');
  this.document_number = page.locator('#id_PersonalData-document_number');
  this.expedition_date = page.locator('#id_PersonalData-expedition_date');
  this.expedition_place = page.locator('#id_PersonalData-expedition_place');
  this.passport_number = page.locator('#id_PersonalData-passport_number');
  this.passport_date = page.locator('#id_PersonalData-passport_date');

  this.birth_day = page.locator('#id_PersonalData-birth_day');
  this.birth_month = page.locator('#id_PersonalData-birth_month');
  this.birth_year = page.locator('#id_PersonalData-birth_year');
  this.relationships = page.locator('#id_PersonalData-relationships');
  this.profession = page.locator('#id_PersonalData-profession');
  this.profesional_id = page.locator('#id_PersonalData-profesional_id');
  this.body_marks = page.locator('#id_PersonalData-body_marks');
  this.height = page.locator('#id_PersonalData-height');
  this.weight = page.locator('#id_PersonalData-weight');
  this.street_type = page.locator('#id_PersonalData-street_type');
  this.principal_number = page.locator('#id_PersonalData-principal_number');
  this.principal_letter = page.locator('#id_PersonalData-principal_letter');
  this.bis = page.locator('#id_PersonalData-bis');
  this.bis_letter = page.locator('#id_PersonalData-bis_letter');
  this.quadrant = page.locator('#id_PersonalData-quadrant');
  this.secondary_number = page.locator('#id_PersonalData-secondary_number');
  this.secondary_letter = page.locator('#id_PersonalData-secondary_letter');
  this.quadrant_2 = page.locator('#id_PersonalData-quadrant_2');
  this.nmbr = page.locator('#id_PersonalData-nmbr');
  this.complement = page.locator('#id_PersonalData-complement');
  this.neighborhood = page.locator('#id_PersonalData-neighborhood');
  this.phone_number = page.locator('#id_PersonalData-phone_number');
  this.landline_phone = page.locator('#id_PersonalData-landline_phone');
  this.city = page.locator('#id_PersonalData-city');
  this.department = page.locator('#id_PersonalData-department');
  this.personal_email = page.locator('#id_PersonalData-personal_email');
  this.formated_address = page.locator('//*[@id="direccion-preview"]');
}

/////HAPPY PATH////

  async FillForm() {

        function generateRandomNumber(digits: number): string {
    const min = Math.pow(10, digits - 1);
    const max = Math.pow(10, digits) - 1;
    return Math.floor(Math.random() * (max - min + 1)) + min + '';
  }

    const UniqueDocument = generateRandomNumber(10);
    const UniquePhone = '3' + generateRandomNumber(9);
    await this.first_name.fill('Brian');
    await this.second_name.fill('Steve');
    await this.lastname.fill('Garnica');
    await this.second_lastname.fill('Sandoval');
    await this.document_type.selectOption('FI');
    await this.document_number.fill(UniqueDocument);
    await this.expedition_date.fill('2018-08-14');
    await this.expedition_place.fill('Bogotá');
    await this.passport_number.fill('Num123456');
    await this.passport_date.fill('2019-05-04');

    await this.birth_day.selectOption('12');
    await this.birth_month.selectOption('8');
    await this.birth_year.fill('2000');
    await this.relationships.selectOption('Common-law marriage');
    await this.profession.fill('Aeronautics Engineer');
    await this.profesional_id.fill('IA123456');
    await this.body_marks.fill('Tatto in the chest, in the arm, in the leg.');
    await this.height.fill('170');
    await this.weight.fill('67')
    await this.street_type.selectOption('Street');
    await this.principal_number.fill('69');
    await this.principal_letter.selectOption('C');
    await this.bis.check();
    await this.bis_letter.selectOption('A');
    await this.quadrant.selectOption('EAST');
    await this.secondary_number.fill('69');
    await this.secondary_letter.selectOption('H');
    await this.quadrant_2.selectOption('WEST');
    await this.nmbr.fill('22');
    await this.complement.fill('Second Floor');
    await this.neighborhood.fill('La strada');
    await this.phone_number.fill(UniquePhone);
    await this.landline_phone.fill('7523491');
    await this.city.fill('Tunja');
    await this.department.fill('Boyacá');
    await this.personal_email.fill('stevegarasdnicas@hotmail.com');
  } 

  async obtainPersonaDataBuiltAddress(): Promise<string> {
  const PersonalDatasBuiltAddress = await this.formated_address.textContent();
  return PersonalDatasBuiltAddress?.trim() ?? '';
}

/////HAPPY PATH////

/////SAD PATH VALIDATORS///
  async FillFormWithErrors() {

  function generateRandomNumber(): string {
  const numero = Math.floor(Math.random() * 1000); // between 0 and 999
  return numero.toString();
}

    const wrongdocument = generateRandomNumber();
    const wrongphone = generateRandomNumber();
    await this.first_name.fill('123');
    await this.second_name.fill('123');
    await this.lastname.fill('123');
    await this.second_lastname.fill('123');
    await this.document_number.fill(wrongdocument);
    await this.expedition_date.fill('2018-08-14');
    await this.expedition_place.fill('123');
    await this.passport_number.fill('x#$"%&%YRTGERFEDC');
    await this.passport_date.fill('2019-05-04');
    await this.birth_year.fill('999999999');
    await this.profession.fill('ADFV3"$RR$#%#EREADSFG#"4234SDF');
    await this.profesional_id.fill('IA12"#"$%$&%YU/&&%3456');
    await this.body_marks.fill('FGBHGNJKIU(/&%$#"WQSASDCFV');
    await this.height.fill('1');
    await this.weight.fill('999999')
    await this.principal_number.fill('622222222222222229');
    await this.secondary_number.fill('6999999999999999999999');
    await this.nmbr.fill('299999999992');
    await this.complement.fill('SADFWR#$T%$#%$WREGFH5');
    await this.neighborhood.fill('!#$"%#$Y&%HGFBVDS');
    await this.phone_number.fill(wrongphone);
    await this.landline_phone.fill('1');
    await this.city.fill('123a#');
    await this.department.fill('123213rewRF#"$');
    await this.personal_email.fill('steve');
  } 

  getErrorMessageForField(fieldId: string): Locator {
    return this.page.locator(`#${fieldId}_error strong`);
  }
/////SAD PATH VALIDATORS///
}