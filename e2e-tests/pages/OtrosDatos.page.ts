import { Page, Locator } from '@playwright/test';

export class OtrosDatosPage {
  readonly page: Page;
  readonly tab: Locator;

  readonly otros_datos_tab : Locator;

//VIAJES AL EXTERIOR

    readonly fecha_viaje_1 : Locator;
    readonly pais_visitado_1  : Locator;
    readonly motivo_1 : Locator;
    readonly permanencia_1 : Locator;

    readonly fecha_viaje_2 : Locator;
    readonly pais_visitado_2  : Locator;
    readonly motivo_2  : Locator;
    readonly permanencia_2 : Locator;

    readonly fecha_viaje_3  : Locator;
    readonly pais_visitado_3 : Locator;
    readonly motivo_3  : Locator;
    readonly permanencia_3  : Locator;

//OTROS DATOS DE INTERÉS
    readonly recomendante  : Locator;
    readonly celular_recomendante  : Locator;
    readonly labora_en_indumil  : Locator;
    readonly nombres_y_apellidos_recomendante_1 : Locator; 
    readonly nombres_y_apellidos_recomendante_2 : Locator;
    readonly cargo_recomendante_1 : Locator;
    readonly cargo_recomendante_2  : Locator;
    readonly unidad_negocio_recomendante_1  : Locator;
    readonly unidad_negocio_recomendante_2  : Locator;

    readonly tipo_via_recomendante  : Locator;
    readonly numero_principal_recomendante  : Locator;
    readonly letra_principal_recomendante : Locator;
    readonly bis_recomendante : Locator;
    readonly letra_bis_recomendante  : Locator;
    readonly cuadrante_recomendante  : Locator;
    readonly numero_secundario_recomendante : Locator;
    readonly letra_secundaria_recomendante : Locator;
    readonly cuadrante_dos_recomendante  : Locator;
    readonly nro_recomendante  : Locator;
    readonly complemento_recomendante  : Locator;
    readonly razon_de_vinculo : Locator;
    readonly direccion_formateada_recomendante : Locator;

    readonly enviar: Locator;

///CONSTRUCTOR///

  constructor(page: Page) {
    this.page = page;
    this.tab = page.locator('text=Situacion Juridica');
    this.otros_datos_tab=page.locator('#formTabs > li:nth-child(9) > button');
//VIAJES AL EXTERIOR
    this.fecha_viaje_1 = page.locator('#id_OtrosDatos-fecha_viaje_1');
    this.pais_visitado_1 = page.locator('#id_OtrosDatos-pais_visitado_1');
    this.motivo_1 = page.locator('#id_OtrosDatos-motivo_1');
    this.permanencia_1 = page.locator('#id_OtrosDatos-permanencia_1');

    this.fecha_viaje_2=page.locator('#id_OtrosDatos-fecha_viaje_2');
    this.pais_visitado_2 = page.locator('#id_OtrosDatos-pais_visitado_2');
    this.motivo_2 = page.locator('#id_OtrosDatos-motivo_2');
    this.permanencia_2 = page.locator('#id_OtrosDatos-permanencia_2');

    this.fecha_viaje_3 = page.locator('#id_OtrosDatos-fecha_viaje_3');
    this.pais_visitado_3 = page.locator('#id_OtrosDatos-pais_visitado_3');
    this.motivo_3 = page.locator('#id_OtrosDatos-motivo_3');
    this.permanencia_3 = page.locator('#id_OtrosDatos-permanencia_3');

//OTROS DATOS DE INTERÉS
    this.recomendante = page.locator('#id_OtrosDatos-recomendante');
    this.tipo_via_recomendante  = page.locator('#id_OtrosDatos-tipo_via_recomendante');
    this.numero_principal_recomendante  = page.locator('#id_OtrosDatos-numero_principal_recomendante');
    this.letra_principal_recomendante = page.locator('#id_OtrosDatos-letra_principal_recomendante');
    this.bis_recomendante = page.locator('#id_OtrosDatos-bis_recomendante');
    this.letra_bis_recomendante  = page.locator('#id_OtrosDatos-letra_bis_recomendante');
    this.cuadrante_recomendante  = page.locator('#id_OtrosDatos-cuadrante_recomendante');
    this.numero_secundario_recomendante = page.locator('#id_OtrosDatos-numero_secundario_recomendante');
    this.letra_secundaria_recomendante = page.locator('#id_OtrosDatos-letra_secundaria_recomendante');
    this.cuadrante_dos_recomendante  = page.locator('#id_OtrosDatos-cuadrante_dos_recomendante');
    this.nro_recomendante  = page.locator('#id_OtrosDatos-nro_recomendante');
    this.complemento_recomendante  = page.locator('#id_OtrosDatos-complemento_recomendante');
    this.direccion_formateada_recomendante = page.locator('#direccion-preview_recomendante');
    this.celular_recomendante  = page.locator('#id_OtrosDatos-celular_recomendante');
    this.labora_en_indumil  = page.locator('#id_OtrosDatos-labora_en_indumil');
    this.nombres_y_apellidos_recomendante_1  = page.locator('#id_OtrosDatos-nombres_y_apellidos_recomendante_1');
    this.nombres_y_apellidos_recomendante_2 = page.locator('#id_OtrosDatos-nombres_y_apellidos_recomendante_2');
    this.cargo_recomendante_1 = page.locator('#id_OtrosDatos-cargo_recomendante_1');
    this.cargo_recomendante_2  = page.locator('#id_OtrosDatos-cargo_recomendante_2');
    this.unidad_negocio_recomendante_1  = page.locator('#id_OtrosDatos-unidad_negocio_recomendante_1');
    this.unidad_negocio_recomendante_2  = page.locator('#id_OtrosDatos-unidad_negocio_recomendante_2');
    this.razon_de_vinculo = page.locator('#id_OtrosDatos-razon_de_vinculo');
    
    this.enviar = page.locator('#wizardForm > button');

  }

  async llenarFormulario() {

    await this.otros_datos_tab.click();
// VIAJES AL EXTERIOR
    await this.fecha_viaje_1.fill('2020-05-22');
    await this.pais_visitado_1.fill('Tailandia');
    await this.motivo_1.fill('Turismo');
    await this.permanencia_1.fill('3 Meses');

    await this.fecha_viaje_2.fill('2021-09-14');
    await this.pais_visitado_2.fill('Indonesia');
    await this.motivo_2.fill('Turismo');
    await this.permanencia_2.fill('1 Mes');

    await this.fecha_viaje_3.fill('2015-05-12');
    await this.pais_visitado_3.fill('Noruega');
    await this.motivo_3.fill('Negocios');
    await this.permanencia_3.fill('2 Semanas'); 

//OTROS DATOS DE INTERÉS
    await this.recomendante.fill('Juan García');

    await this.tipo_via_recomendante.selectOption('Calle');
    await this.numero_principal_recomendante.fill('23');
    await this.letra_principal_recomendante.selectOption('B');
    await this.bis_recomendante.check();
    await this.letra_bis_recomendante.selectOption('C');
    await this.cuadrante_recomendante.selectOption('ESTE');
    await this.numero_secundario_recomendante.fill('14');
    await this.letra_secundaria_recomendante.selectOption('F');
    await this.cuadrante_dos_recomendante.selectOption('NORTE');
    await this.nro_recomendante.fill('122');
    await this.complemento_recomendante.fill('Tercer Piso Apartamento 232');

  
    await this.celular_recomendante.fill('3216549877');
    await this.labora_en_indumil.selectOption('Sí');
    await this.nombres_y_apellidos_recomendante_1.fill('Juan García Melo'); 
    await this.nombres_y_apellidos_recomendante_2.fill('Diana Espitia Gonzales');
    await this.cargo_recomendante_1.fill('Gerente');
    await this.cargo_recomendante_2.fill('Profesional');
    await this.unidad_negocio_recomendante_1.fill('OC'); 
    await this.unidad_negocio_recomendante_2.fill('FASAB');
    await this.razon_de_vinculo.fill('porque blablablabal y también porque babalblablablablablablablaba porque de hecho balbalbalbalba entones blablablablbala y pues por lo tanto blablablaba');

    

    
  } 

      async obtenerDireccionFormateadaRecomendante(): Promise<string> {
  const DireccionFormateadaRecomendante = await this.direccion_formateada_recomendante.textContent();
  return DireccionFormateadaRecomendante?.trim() ?? '';

}

}