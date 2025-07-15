import { Page, Locator } from '@playwright/test';

export class InformacionAcademicaPage {
  readonly page: Page;
  readonly tab: Locator;

  readonly informacion_academica_tab :Locator;
//ESTUDIOS REALIZADOS

  readonly estudios_1 : Locator;
  readonly año_estudios_1 : Locator;
  readonly titulo_estudios_1 :  Locator;
  readonly nombre_institucion_estudios_1 : Locator;
  readonly ciudad_estudios_1 : Locator;

  readonly estudios_2 : Locator;
  readonly año_estudios_2 : Locator;
  readonly titulo_estudios_2 :  Locator;
  readonly nombre_institucion_estudios_2 : Locator;
  readonly ciudad_estudios_2 : Locator;



//IDIOMAS EXTRANJEROS
  
  readonly idioma_extranjero_1 : Locator;
  readonly lee_idioma_extranjero_1 : Locator;
  readonly habla_idioma_extranjero_1 :  Locator;
  readonly escribe_idioma_extranjero_1 : Locator;


  readonly idioma_extranjero_2 : Locator;
  readonly lee_idioma_extranjero_2 : Locator;
  readonly habla_idioma_extranjero_2 :  Locator;
  readonly escribe_idioma_extranjero_2 : Locator;

//ESPECIALIDADES EN SISTEMAS
  
  readonly word_check :Locator;
  readonly excel_check :Locator;
  readonly powerpoint_check :Locator;
  readonly access_check :Locator;
  readonly internet_check :Locator;
  readonly otro_check:Locator;

constructor(page: Page) {
    this.page = page;
    this.tab = page.locator('text=Informacion Academica');
    this.informacion_academica_tab=page.locator('#formTabs > li:nth-child(3) > button');
//ESTUDIOS REALIZADOS

    this.estudios_1 = page.locator('#id_InformacionAcademica-estudios_1');                  
    this.año_estudios_1 = page.locator('#id_InformacionAcademica-año_estudios_1');
    this.titulo_estudios_1 = page.locator('#id_InformacionAcademica-titulo_estudios_1');
    this.nombre_institucion_estudios_1 = page.locator('#id_InformacionAcademica-nombre_institucion_estudios_1');
    this.ciudad_estudios_1 = page.locator('#id_InformacionAcademica-ciudad_estudios_1');

    this.estudios_2 = page.locator('#id_InformacionAcademica-estudios_2');
    this.año_estudios_2 = page.locator('#id_InformacionAcademica-año_estudios_2');
    this.titulo_estudios_2 = page.locator('#id_InformacionAcademica-titulo_estudios_2');
    this.nombre_institucion_estudios_2 = page.locator('#id_InformacionAcademica-nombre_institucion_estudios_2');
    this.ciudad_estudios_2 = page.locator('#id_InformacionAcademica-ciudad_estudios_2');

//IDIOMAS EXTRANJEROS

    this.idioma_extranjero_1 = page.locator('#id_InformacionAcademica-idioma_extranjero_1');
    this.lee_idioma_extranjero_1 = page.locator('#id_InformacionAcademica-lee_idioma_extranjero_1');
    this.habla_idioma_extranjero_1 = page.locator('#id_InformacionAcademica-habla_idioma_extranjero_1');
    this.escribe_idioma_extranjero_1 = page.locator('#id_InformacionAcademica-escribe_idioma_extranjero_1');

    this.idioma_extranjero_2 = page.locator('#id_InformacionAcademica-idioma_extranjero_2');
    this.lee_idioma_extranjero_2 = page.locator('#id_InformacionAcademica-lee_idioma_extranjero_2');
    this.habla_idioma_extranjero_2 = page.locator('#id_InformacionAcademica-habla_idioma_extranjero_2');
    this.escribe_idioma_extranjero_2 = page.locator('#id_InformacionAcademica-escribe_idioma_extranjero_2');


//ESPECIALIDADES EN SISTEMAS

   this.word_check = page.locator('#id_InformacionAcademica-word_check'); 
   this.excel_check = page.locator('#id_InformacionAcademica-excel_check');
   this.powerpoint_check = page.locator('#id_InformacionAcademica-powerpoint_check');
   this.access_check = page.locator('#id_InformacionAcademica-access_check'); 
   this.internet_check = page.locator('#id_InformacionAcademica-internet_check'); 
   this.otro_check = page.locator('#id_InformacionAcademica-otro_check');

  }


  async llenarFormulario() {


    await this.informacion_academica_tab.click();
//ESTUDIOS REALIZADOS
    await this.estudios_1.fill('Bachillerato');
    await this.año_estudios_1.fill('2018');
    await this.titulo_estudios_1.fill('Bachiller Académico Bilingüe');
    await this.nombre_institucion_estudios_1.fill('Colegio CAFAM');
    await this.ciudad_estudios_1.fill('Bogotá');

    await this.estudios_2.fill('Profesional');
    await this.año_estudios_2.fill('2024');
    await this.titulo_estudios_2.fill('Ingeniero aeronáutico');
    await this.nombre_institucion_estudios_2.fill('Escuela de Aviación Del Ejército');
    await this.ciudad_estudios_2.fill('Bogotá');


//IDIOMAS EXTRANJEROS

    await this.idioma_extranjero_1.fill('Inglés');
    await this.lee_idioma_extranjero_1.selectOption('Sí');
    await this.habla_idioma_extranjero_1.selectOption('Sí');
    await this.escribe_idioma_extranjero_1.selectOption('Sí');

    await this.idioma_extranjero_2.fill('Chino');
    await this.lee_idioma_extranjero_2.selectOption('No');
    await this.habla_idioma_extranjero_2.selectOption('No');
    await this.escribe_idioma_extranjero_2.selectOption('No');

//ESPECIALIDADES EN SISTEMAS

   await this.word_check.selectOption('Sí');
   await this.excel_check.selectOption('Sí');
   await this.powerpoint_check.selectOption('Sí');
   await this.access_check.selectOption('No');
   await this.internet_check.selectOption('No');
   await this.otro_check.fill('Playwright, Django, Uipath');
  } 



      async FillFormWithErrors() {

   await this.informacion_academica_tab.click();

//ESTUDIOS REALIZADOS
    await this.estudios_1.fill('EDWFDGFBYY&%$#""');
    await this.año_estudios_1.fill('2');
    await this.titulo_estudios_1.fill('EDWFDGFBYY&%$#""');
    await this.nombre_institucion_estudios_1.fill('EDWFDGFBYY&%$#""');
    await this.ciudad_estudios_1.fill('EDWFDGFBYY&%$#""');

    await this.estudios_2.fill('EDWFDGFBYY&%$#""');
    await this.año_estudios_2.fill('99999999999999999999999999999999999999999');
    await this.titulo_estudios_2.fill('EDWFDGFBYY&%$#""');
    await this.nombre_institucion_estudios_2.fill('EDWFDGFBYY&%$#""');
    await this.ciudad_estudios_2.fill('EDWFDGFBYY&%$#""');


//IDIOMAS EXTRANJEROS

    await this.idioma_extranjero_1.fill('EDWFDGFBYY&%$#');
    await this.idioma_extranjero_2.fill('EDWFDGFBYY&%$#');


//ESPECIALIDADES EN SISTEMAS

   await this.otro_check.fill('EDWFDGFBYY&%$#""');
  
      }
}