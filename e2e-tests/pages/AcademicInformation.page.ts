import { Page, Locator } from '@playwright/test';

export class AcademicInformationPage {
  readonly page: Page;
  readonly tab: Locator;

  readonly academic_information_tab :Locator;
//ESTUDIOS REALIZADOS

  readonly studies_1 : Locator;
  readonly studies_1_year : Locator;
  readonly studies_title_1 :  Locator;
  readonly studies_institution_name_1 : Locator;
  readonly studies_city_1 : Locator;

  readonly studies_2 : Locator;
  readonly studies_2_year : Locator;
  readonly studies_title_2 :  Locator;
  readonly studies_institution_name_2 : Locator;
  readonly studies_city_2 : Locator;



//IDIOMAS EXTRANJEROS
  
  readonly foreign_language_1 : Locator;
  readonly can_read_foreign_language_1 : Locator;
  readonly can_speak_foreign_language_1 :  Locator;
  readonly can_write_foreign_language_1 : Locator;


  readonly foreign_language_2 : Locator;
  readonly can_read_foreign_language_2 : Locator;
  readonly can_speak_foreign_language_2 :  Locator;
  readonly can_write_foreign_language_2 : Locator;

//ESPECIALIDADES EN SISTEMAS
  
  readonly word_check :Locator;
  readonly excel_check :Locator;
  readonly powerpoint_check :Locator;
  readonly access_check :Locator;
  readonly internet_check :Locator;
  readonly other_check:Locator;

constructor(page: Page) {
    this.page = page;
    this.tab = page.locator('text=Informacion Academica');
    this.academic_information_tab=page.locator('#formTabs > li:nth-child(3) > button');
//ESTUDIOS REALIZADOS

    this.studies_1 = page.locator('#id_AcademicInformation-studies_1');
    this.studies_1_year = page.locator('#id_AcademicInformation-studies_1_year');
    this.studies_title_1 = page.locator('#id_AcademicInformation-studies_title_1');
    this.studies_institution_name_1 = page.locator('#id_AcademicInformation-studies_institution_name_1');
    this.studies_city_1 = page.locator('#id_AcademicInformation-studies_city_1');

    this.studies_2 = page.locator('#id_AcademicInformation-studies_2');
    this.studies_2_year = page.locator('#id_AcademicInformation-studies_2_year');
    this.studies_title_2 = page.locator('#id_AcademicInformation-studies_title_2');
    this.studies_institution_name_2 = page.locator('#id_AcademicInformation-studies_institution_name_2');
    this.studies_city_2 = page.locator('#id_AcademicInformation-studies_city_2');

// FOREIGN LANGUAGES

this.foreign_language_1 = page.locator('#id_AcademicInformation-foreign_language_1');
this.can_read_foreign_language_1 = page.locator('#id_AcademicInformation-can_read_foreign_language_1');
this.can_speak_foreign_language_1 = page.locator('#id_AcademicInformation-can_speak_foreign_language_1');
this.can_write_foreign_language_1 = page.locator('#id_AcademicInformation-can_write_foreign_language_1');

this.foreign_language_2 = page.locator('#id_AcademicInformation-foreign_language_2');
this.can_read_foreign_language_2 = page.locator('#id_AcademicInformation-can_read_foreign_language_2');
this.can_speak_foreign_language_2 = page.locator('#id_AcademicInformation-can_speak_foreign_language_2');
this.can_write_foreign_language_2 = page.locator('#id_AcademicInformation-can_write_foreign_language_2');



// OFFICE TOOLS SKILLS

this.word_check = page.locator('#id_AcademicInformation-word_check'); 
this.excel_check = page.locator('#id_AcademicInformation-excel_check');
this.powerpoint_check = page.locator('#id_AcademicInformation-powerpoint_check');
this.access_check = page.locator('#id_AcademicInformation-access_check'); 
this.internet_check = page.locator('#id_AcademicInformation-internet_check'); 
this.other_check = page.locator('#id_AcademicInformation-other_check');


  }


  async FillForm() {


    await this.academic_information_tab.click();
//ESTUDIOS REALIZADOS
    await this.studies_1.fill('College');
    await this.studies_1_year.fill('2018');
    await this.studies_title_1.fill('bilingual bachelor degree');
    await this.studies_institution_name_1.fill('CAFAM school');
    await this.studies_city_1.fill('Bogotá');

    await this.studies_2.fill('Professional');
    await this.studies_2_year.fill('2024');
    await this.studies_title_2.fill('Aeronautics Engineer');
    await this.studies_institution_name_2.fill('ESAVE');
    await this.studies_city_2.fill('Bogotá');


//IDIOMAS EXTRANJEROS

    await this.foreign_language_1.fill('Español');
    await this.can_read_foreign_language_1.selectOption('Yes');
    await this.can_speak_foreign_language_1.selectOption('Yes');
    await this.can_write_foreign_language_1.selectOption('Yes');

    await this.foreign_language_2.fill('Chinese');
    await this.can_read_foreign_language_2.selectOption('No');
    await this.can_speak_foreign_language_2.selectOption('No');
    await this.can_write_foreign_language_2.selectOption('No');

//ESPECIALIDADES EN SISTEMAS

   await this.word_check.selectOption('Yes');
   await this.excel_check.selectOption('No');
   await this.powerpoint_check.selectOption('Yes');
   await this.access_check.selectOption('No');
   await this.internet_check.selectOption('No');
   await this.other_check.fill('Playwright, Django, Uipath');
  } 



      async FillFormWithErrors() {

   await this.academic_information_tab.click();

//ESTUDIOS REALIZADOS
    await this.studies_1.fill('EDWFDGFBYY&%$#""');
    await this.studies_1_year.fill('2');
    await this.studies_title_1.fill('EDWFDGFBYY&%$#""');
    await this.studies_institution_name_1.fill('EDWFDGFBYY&%$#""');
    await this.studies_city_1.fill('EDWFDGFBYY&%$#""');

    await this.studies_2.fill('EDWFDGFBYY&%$#""');
    await this.studies_2_year.fill('99999999999999999999999999999999999999999');
    await this.studies_title_2.fill('EDWFDGFBYY&%$#""');
    await this.studies_institution_name_2.fill('EDWFDGFBYY&%$#""');
    await this.studies_city_2.fill('EDWFDGFBYY&%$#""');


//IDIOMAS EXTRANJEROS

    await this.foreign_language_1.fill('EDWFDGFBYY&%$#');
    await this.foreign_language_2.fill('EDWFDGFBYY&%$#');


//ESPECIALIDADES EN SISTEMAS

   await this.other_check.fill('EDWFDGFBYY&%$#""');
  
      }
}