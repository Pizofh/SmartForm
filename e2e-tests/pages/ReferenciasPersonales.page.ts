import { Page, Locator } from '@playwright/test';

export class ReferenciasPersonalesPage {
  readonly page: Page;
  readonly tab: Locator;

  readonly referencias_personales_tab :Locator;
// REFERENCIA 1
  readonly nombre_referencia_1: Locator;
  readonly ocupacion_referencia_1: Locator;
  readonly empresa_referencia_1: Locator;
  readonly tiempo_referencia_1: Locator;
  readonly ciudad_referencia_1: Locator;
  readonly telefono_referencia_1: Locator;
  readonly tipo_via_referencia_1: Locator;
  readonly numero_principal_referencia_1: Locator;
  readonly letra_principal_referencia_1: Locator;
  readonly bis_referencia_1: Locator;
  readonly letra_bis_referencia_1: Locator;
  readonly cuadrante_referencia_1: Locator;
  readonly numero_secundario_referencia_1: Locator;
  readonly letra_secundaria_referencia_1: Locator;
  readonly cuadrante_dos_referencia_1: Locator;
  readonly nro_referencia_1: Locator;
  readonly complemento_referencia_1: Locator;
  readonly direccion_formateada_referencia_1: Locator;

//REFERENCIA 2
  readonly nombre_referencia_2: Locator;
  readonly ocupacion_referencia_2: Locator;
  readonly empresa_referencia_2: Locator;
  readonly tiempo_referencia_2: Locator;
  readonly ciudad_referencia_2: Locator;
  readonly telefono_referencia_2: Locator;
  readonly tipo_via_referencia_2: Locator;
  readonly numero_principal_referencia_2: Locator;
  readonly letra_principal_referencia_2: Locator;
  readonly bis_referencia_2: Locator;
  readonly letra_bis_referencia_2: Locator;
  readonly cuadrante_referencia_2: Locator;
  readonly numero_secundario_referencia_2: Locator;
  readonly letra_secundaria_referencia_2: Locator;
  readonly  cuadrante_dos_referencia_2: Locator;
  readonly nro_referencia_2: Locator;
  readonly complemento_referencia_2: Locator;
  readonly direccion_formateada_referencia_2: Locator;

//REFERENCIA 3
  readonly nombre_referencia_3: Locator;
  readonly ocupacion_referencia_3: Locator;
  readonly empresa_referencia_3: Locator;
  readonly tiempo_referencia_3: Locator;
  readonly ciudad_referencia_3: Locator;
  readonly telefono_referencia_3: Locator;
  readonly tipo_via_referencia_3: Locator;
  readonly numero_principal_referencia_3: Locator;
  readonly letra_principal_referencia_3: Locator;
  readonly bis_referencia_3: Locator;
  readonly letra_bis_referencia_3: Locator;
  readonly cuadrante_referencia_3: Locator;
  readonly numero_secundario_referencia_3: Locator;
  readonly letra_secundaria_referencia_3: Locator;
  readonly  cuadrante_dos_referencia_3: Locator;
  readonly nro_referencia_3: Locator;
  readonly complemento_referencia_3: Locator;
  readonly direccion_formateada_referencia_3: Locator;

constructor(page: Page) {
    this.page = page;
    this.tab = page.locator('text=Referencias Personales');
    this.referencias_personales_tab =page.locator('#formTabs > li:nth-child(5) > button');

//REFERENCIA 1
    this.nombre_referencia_1 = page.locator('#id_ReferenciasPersonales-nombre_referencia_1');
    this.ocupacion_referencia_1 = page.locator('#id_ReferenciasPersonales-ocupacion_referencia_1');
    this.empresa_referencia_1 = page.locator('#id_ReferenciasPersonales-empresa_referencia_1');
    this.tiempo_referencia_1 = page.locator('#id_ReferenciasPersonales-tiempo_referencia_1');
    this.ciudad_referencia_1 = page.locator('#id_ReferenciasPersonales-ciudad_referencia_1');
    this.telefono_referencia_1 = page.locator('#id_ReferenciasPersonales-telefono_referencia_1');
    this.tipo_via_referencia_1 = page.locator('#id_ReferenciasPersonales-tipo_via_referencia_1');
    this.numero_principal_referencia_1 = page.locator('#id_ReferenciasPersonales-numero_principal_referencia_1');
    this.letra_principal_referencia_1 = page.locator('#id_ReferenciasPersonales-letra_principal_referencia_1');
    this.bis_referencia_1 = page.locator('#id_ReferenciasPersonales-bis_referencia_1');
    this.letra_bis_referencia_1 = page.locator('#id_ReferenciasPersonales-letra_bis_referencia_1');
    this.cuadrante_referencia_1 = page.locator('#id_ReferenciasPersonales-cuadrante_referencia_1');
    this.numero_secundario_referencia_1 = page.locator('#id_ReferenciasPersonales-numero_secundario_referencia_1');
    this.letra_secundaria_referencia_1 = page.locator('#id_ReferenciasPersonales-letra_secundaria_referencia_1');
    this.cuadrante_dos_referencia_1 = page.locator('#id_ReferenciasPersonales-cuadrante_dos_referencia_1');
    this.nro_referencia_1 = page.locator('#id_ReferenciasPersonales-nro_referencia_1');
    this.complemento_referencia_1 = page.locator('#id_ReferenciasPersonales-complemento_referencia_1');
    this.direccion_formateada_referencia_1 = page.locator('#direccion-preview_referencia_1');

//REFERENCIA 2
    this.nombre_referencia_2 = page.locator('#id_ReferenciasPersonales-nombre_referencia_2');
    this.ocupacion_referencia_2= page.locator('#id_ReferenciasPersonales-ocupacion_referencia_2');
    this.empresa_referencia_2 = page.locator('#id_ReferenciasPersonales-empresa_referencia_2');
    this.tiempo_referencia_2 = page.locator('#id_ReferenciasPersonales-tiempo_referencia_2');
    this.ciudad_referencia_2 = page.locator('#id_ReferenciasPersonales-ciudad_referencia_2');
    this.telefono_referencia_2 = page.locator('#id_ReferenciasPersonales-telefono_referencia_2');
    this.tipo_via_referencia_2 = page.locator('#id_ReferenciasPersonales-tipo_via_referencia_2');
    this.numero_principal_referencia_2 = page.locator('#id_ReferenciasPersonales-numero_principal_referencia_2');
    this.letra_principal_referencia_2 = page.locator('#id_ReferenciasPersonales-letra_principal_referencia_2');
    this.bis_referencia_2 = page.locator('#id_ReferenciasPersonales-bis_referencia_2');
    this.letra_bis_referencia_2 = page.locator('#id_ReferenciasPersonales-letra_bis_referencia_2');
    this.cuadrante_referencia_2 = page.locator('#id_ReferenciasPersonales-cuadrante_referencia_2');
    this.numero_secundario_referencia_2 = page.locator('#id_ReferenciasPersonales-numero_secundario_referencia_2');
    this.letra_secundaria_referencia_2 = page.locator('#id_ReferenciasPersonales-letra_secundaria_referencia_2');
    this.cuadrante_dos_referencia_2 = page.locator('#id_ReferenciasPersonales-cuadrante_dos_referencia_2');
    this.nro_referencia_2 = page.locator('#id_ReferenciasPersonales-nro_referencia_2');
    this.complemento_referencia_2 = page.locator('#id_ReferenciasPersonales-complemento_referencia_2');
    this.direccion_formateada_referencia_2 =page.locator('#direccion-preview_referencia_2');

//REFERENCIA 3
    this.nombre_referencia_3 = page.locator('#id_ReferenciasPersonales-nombre_referencia_3');
    this.ocupacion_referencia_3 = page.locator('#id_ReferenciasPersonales-ocupacion_referencia_3');
    this.empresa_referencia_3 = page.locator('#id_ReferenciasPersonales-empresa_referencia_3');
    this.tiempo_referencia_3 = page.locator('#id_ReferenciasPersonales-tiempo_referencia_3');
    this.ciudad_referencia_3 = page.locator('#id_ReferenciasPersonales-ciudad_referencia_3');
    this.telefono_referencia_3 = page.locator('#id_ReferenciasPersonales-telefono_referencia_3');
    this.tipo_via_referencia_3 = page.locator('#id_ReferenciasPersonales-tipo_via_referencia_3');
    this.numero_principal_referencia_3 = page.locator('#id_ReferenciasPersonales-numero_principal_referencia_3');
    this.letra_principal_referencia_3 = page.locator('#id_ReferenciasPersonales-letra_principal_referencia_3');
    this.bis_referencia_3 = page.locator('#id_ReferenciasPersonales-bis_referencia_3');
    this.letra_bis_referencia_3 = page.locator('#id_ReferenciasPersonales-letra_bis_referencia_3');
    this.cuadrante_referencia_3 = page.locator('#id_ReferenciasPersonales-cuadrante_referencia_3');
    this.numero_secundario_referencia_3 = page.locator('#id_ReferenciasPersonales-numero_secundario_referencia_3');
    this.letra_secundaria_referencia_3 = page.locator('#id_ReferenciasPersonales-letra_secundaria_referencia_3');
    this.cuadrante_dos_referencia_3 = page.locator('#id_ReferenciasPersonales-cuadrante_dos_referencia_3');
    this.nro_referencia_3 = page.locator('#id_ReferenciasPersonales-nro_referencia_3');
    this.complemento_referencia_3 = page.locator('#id_ReferenciasPersonales-complemento_referencia_3');
    this.direccion_formateada_referencia_3 = page.locator('#direccion-preview_referencia_3');
  }


  async llenarFormulario() {
    await this.referencias_personales_tab.click();
//REFERENCIA 1
    await this.nombre_referencia_1.fill('Samuel Sabogal Pardo');
    await this.ocupacion_referencia_1.fill('Lord Commander');
    await this.empresa_referencia_1.fill('Cyte');
    await this.tiempo_referencia_1.fill('3');
    await this.ciudad_referencia_1.fill('Bogotá');
    await this.telefono_referencia_1.fill('312457895');
    await this.tipo_via_referencia_1.selectOption('Calle');
    await this.numero_principal_referencia_1.fill('12');
    await this.letra_principal_referencia_1.selectOption('B');
    await this.bis_referencia_1.check();
    await this.letra_bis_referencia_1.selectOption('A');
    await this.cuadrante_referencia_1.selectOption('OESTE');
    await this.numero_secundario_referencia_1.fill('45');
    await this.letra_secundaria_referencia_1.selectOption('H');
    await this.cuadrante_dos_referencia_1.selectOption('OESTE');
    await this.nro_referencia_1.fill('456');
    await this.complemento_referencia_1.fill('APTO 987');

//REFERENCIA 2
    await this.nombre_referencia_2.fill('ANGELA TOFIÑO');
    await this.ocupacion_referencia_2.fill('ABOGADA');
    await this.empresa_referencia_2.fill('DIGSA');
    await this.tiempo_referencia_2.fill('5');
    await this.ciudad_referencia_2.fill('BOgotá');
    await this.telefono_referencia_2.fill('3216549878');
    await this.tipo_via_referencia_2.selectOption('Carrera');
    await this.numero_principal_referencia_2.fill('56');
    await this.letra_principal_referencia_2.selectOption('H');
    await this.bis_referencia_2.uncheck();
    await this.letra_bis_referencia_2.selectOption('');
    await this.cuadrante_referencia_2.selectOption('NORTE');
    await this.numero_secundario_referencia_2.fill('23');
    await this.letra_secundaria_referencia_2.selectOption('L');
    await this.cuadrante_dos_referencia_2.selectOption('SUR');
    await this.nro_referencia_2.fill('457');
    await this.complemento_referencia_2.fill('SEGUNDO PISO');

//REFERENCIA 3
    await this.nombre_referencia_3.fill('NOMBREEE');
    await this.ocupacion_referencia_3.fill('OCUPAciónnnn');
    await this.empresa_referencia_3.fill('empresaficticia');
    await this.tiempo_referencia_3.fill('9');
    await this.ciudad_referencia_3.fill('Tokio');
    await this.telefono_referencia_3.fill('3219876545');
    await this.tipo_via_referencia_3.selectOption('Avenida');
    await this.numero_principal_referencia_3.fill('89');
    await this.letra_principal_referencia_3.selectOption('G');
    await this.bis_referencia_3.check();
    await this.letra_bis_referencia_3.selectOption('Y');
    await this.cuadrante_referencia_3.selectOption('SUR');
    await this.numero_secundario_referencia_3.fill('56');
    await this.letra_secundaria_referencia_3.selectOption('Q');
    await this.cuadrante_dos_referencia_3.selectOption('ESTE');
    await this.nro_referencia_3.fill('85');
    await this.complemento_referencia_3.fill('APARTAMENTO OOOO OOOO');
  } 

  async obtenerDireccionFormateadaReferencia1(): Promise<string> {
  const DireccionFormateadaReferencia1 = await this.direccion_formateada_referencia_1.textContent();
  return DireccionFormateadaReferencia1?.trim() ?? '';
}
  async obtenerDireccionFormateadaReferencia2(): Promise<string> {
  const DireccionFormateadaReferencia2= await this.direccion_formateada_referencia_2.textContent();
  return DireccionFormateadaReferencia2?.trim() ?? '';
}
  async obtenerDireccionFormateadaReferencia3(): Promise<string> {
  const DireccionFormateadaReferencia3 = await this.direccion_formateada_referencia_3.textContent();
  return DireccionFormateadaReferencia3?.trim() ?? '';
}

}