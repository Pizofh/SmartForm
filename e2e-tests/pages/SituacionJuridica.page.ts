import { Page, Locator } from '@playwright/test';

export class SituacionJuridicaPage {
  readonly page: Page;
  readonly tab: Locator;

  readonly situacion_juridica_tab : Locator;
  readonly fecha_proceso_1  : Locator;
  readonly tipo_de_investigacion_1  : Locator;
  readonly causa_1 : Locator;
  readonly autoridad_1  : Locator;
  readonly estado_del_proceso_1  : Locator;
  readonly responsable_1  : Locator;

  readonly fecha_proceso_2  : Locator;
  readonly tipo_de_investigacion_2  : Locator;
  readonly causa_2 : Locator;
  readonly autoridad_2  : Locator;
  readonly estado_del_proceso_2 : Locator;
  readonly responsable_2 : Locator;



  constructor(page: Page) {
    this.page = page;
    this.tab = page.locator('text=Situacion Juridica');
    this.situacion_juridica_tab=page.locator('#formTabs > li:nth-child(7) > button');


    this.fecha_proceso_1 = page.locator('#id_SituacionJuridica-fecha_proceso_1');
    this.tipo_de_investigacion_1  = page.locator('#id_SituacionJuridica-tipo_de_investigacion_1');
    this.causa_1 = page.locator('#id_SituacionJuridica-causa_1');
    this.autoridad_1  = page.locator('#id_SituacionJuridica-autoridad_1');
    this.estado_del_proceso_1 = page.locator('#id_SituacionJuridica-estado_del_proceso_1'); 
    this.responsable_1  = page.locator('#id_SituacionJuridica-responsable_1');

    this.fecha_proceso_2  = page.locator('#id_SituacionJuridica-fecha_proceso_2');
    this.tipo_de_investigacion_2  = page.locator('#id_SituacionJuridica-tipo_de_investigacion_2');
    this.causa_2 = page.locator('#id_SituacionJuridica-causa_2');
    this.autoridad_2  = page.locator('#id_SituacionJuridica-autoridad_2');
    this.estado_del_proceso_2 = page.locator('#id_SituacionJuridica-estado_del_proceso_2');
    this.responsable_2 = page.locator('#id_SituacionJuridica-responsable_2');


  }


  async llenarFormulario() {
    await this.situacion_juridica_tab.click();
    await this.fecha_proceso_1.fill('2019-05-22');
    await this.tipo_de_investigacion_1.fill('Legal');
    await this.causa_1.fill('Causa 1 de investigación');
    await this.autoridad_1.fill('Contraloría');
    await this.estado_del_proceso_1.fill('En proceso');
    await this.responsable_1.selectOption('No');

    await this.fecha_proceso_2.fill('2014-02-22');
    await this.tipo_de_investigacion_2.fill('Legal');
    await this.causa_2.fill('Causa 2 de investigación');
    await this.autoridad_2.fill('Procuraduría');
    await this.estado_del_proceso_2.fill('En proceso');
    await this.responsable_2.selectOption('Sí');


  } 


}

