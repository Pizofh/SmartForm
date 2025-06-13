import { Page, Locator } from '@playwright/test';

export class DireccionesAnterioresPage {
  readonly page: Page;
  readonly tab: Locator;

  readonly direcciones_anteriores_tab : Locator;
  readonly desde_1 : Locator;
  readonly hasta_1 : Locator;
  readonly tipo_via_anterior_1: Locator; 
  readonly numero_principal_anterior_1: Locator; 
  readonly letra_principal_anterior_1: Locator; 
  readonly bis_anterior_1: Locator; 
  readonly letra_bis_anterior_1: Locator; 
  readonly cuadrante_anterior_1: Locator; 
  readonly numero_secundario_anterior_1: Locator;
  readonly letra_secundaria_anterior_1: Locator; 
  readonly cuadrante_dos_anterior_1: Locator;
  readonly nro_anterior_1: Locator; 
  readonly complemento_anterior_1: Locator; 
  readonly direccion_completa_anterior_1: Locator;
  readonly telefono_direccion_anterior_1_1: Locator;
  readonly telefono_direccion_anterior_1_2: Locator;
  readonly ciudad_direccion_anterior_1 : Locator;

  readonly desde_2 : Locator; 
  readonly hasta_2 : Locator;
  readonly tipo_via_anterior_2: Locator; 
  readonly numero_principal_anterior_2: Locator; 
  readonly letra_principal_anterior_2: Locator; 
  readonly bis_anterior_2: Locator; 
  readonly letra_bis_anterior_2: Locator; 
  readonly cuadrante_anterior_2: Locator; 
  readonly numero_secundario_anterior_2: Locator;
  readonly letra_secundaria_anterior_2: Locator; 
  readonly cuadrante_dos_anterior_2: Locator;
  readonly nro_anterior_2: Locator; 
  readonly complemento_anterior_2: Locator; 
  readonly direccion_completa_anterior_2: Locator;
  readonly telefono_direccion_anterior_2_1: Locator;
  readonly telefono_direccion_anterior_2_2: Locator;
  readonly ciudad_direccion_anterior_2 : Locator;



  constructor(page: Page) {
    this.page = page;
    this.tab = page.locator('text=Direcciones Anteriores');
    this.direcciones_anteriores_tab=page.locator('#formTabs > li:nth-child(2) > button');

    this.desde_1 = page.locator('#id_DireccionesAnteriores-desde_1')
    this.hasta_1 = page.locator('#id_DireccionesAnteriores-hasta_1');
    this.tipo_via_anterior_1 = page.locator('#id_DireccionesAnteriores-tipo_via_anterior_1')
    this.numero_principal_anterior_1 = page.locator('#id_DireccionesAnteriores-numero_principal_anterior_1');
    this.letra_principal_anterior_1 = page.locator('#id_DireccionesAnteriores-letra_principal_anterior_1');
    this.bis_anterior_1 = page.locator('#id_DireccionesAnteriores-bis_anterior_1');
    this.letra_bis_anterior_1 = page.locator('#id_DireccionesAnteriores-letra_bis_anterior_1');
    this.cuadrante_anterior_1 = page.locator('#id_DireccionesAnteriores-cuadrante_anterior_1');
    this.numero_secundario_anterior_1 = page.locator('#id_DireccionesAnteriores-numero_secundario_anterior_1');
    this.letra_secundaria_anterior_1 = page.locator('#id_DireccionesAnteriores-letra_secundaria_anterior_1');
    this.cuadrante_dos_anterior_1 = page.locator('#id_DireccionesAnteriores-cuadrante_dos_anterior_1');
    this.nro_anterior_1 = page.locator('#id_DireccionesAnteriores-nro_anterior_1');
    this.complemento_anterior_1 = page.locator('#id_DireccionesAnteriores-complemento_anterior_1');
    this.direccion_completa_anterior_1 = page.locator('#direccion-preview_anterior_1');
    this.telefono_direccion_anterior_1_1 = page.locator('#id_DireccionesAnteriores-telefono_direccion_anterior_1_1') 
    this.telefono_direccion_anterior_1_2 = page.locator('#id_DireccionesAnteriores-telefono_direccion_anterior_1_2')
    this.ciudad_direccion_anterior_1 = page.locator('#id_DireccionesAnteriores-ciudad_direccion_anterior_1')

    this.desde_2 = page.locator('#id_DireccionesAnteriores-desde_2')
    this.hasta_2 = page.locator('#id_DireccionesAnteriores-hasta_2');
    this.tipo_via_anterior_2 = page.locator('#id_DireccionesAnteriores-tipo_via_anterior_2')
    this.numero_principal_anterior_2 = page.locator('#id_DireccionesAnteriores-numero_principal_anterior_2');
    this.letra_principal_anterior_2 = page.locator('#id_DireccionesAnteriores-letra_principal_anterior_2');
    this.bis_anterior_2 = page.locator('#id_DireccionesAnteriores-bis_anterior_2');
    this.letra_bis_anterior_2 = page.locator('#id_DireccionesAnteriores-letra_bis_anterior_2');
    this.cuadrante_anterior_2 = page.locator('#id_DireccionesAnteriores-cuadrante_anterior_2');
    this.numero_secundario_anterior_2 = page.locator('#id_DireccionesAnteriores-numero_secundario_anterior_2');
    this.letra_secundaria_anterior_2 = page.locator('#id_DireccionesAnteriores-letra_secundaria_anterior_2');
    this.cuadrante_dos_anterior_2 = page.locator('#id_DireccionesAnteriores-cuadrante_dos_anterior_2');
    this.nro_anterior_2 = page.locator('#id_DireccionesAnteriores-nro_anterior_2');
    this.complemento_anterior_2 = page.locator('#id_DireccionesAnteriores-complemento_anterior_2');
    this.direccion_completa_anterior_2 = page.locator('#direccion-preview_anterior_2');
    this.telefono_direccion_anterior_2_1 = page.locator('#id_DireccionesAnteriores-telefono_direccion_anterior_2_1') 
    this.telefono_direccion_anterior_2_2 = page.locator('#id_DireccionesAnteriores-telefono_direccion_anterior_2_2')
    this.ciudad_direccion_anterior_2 = page.locator('#id_DireccionesAnteriores-ciudad_direccion_anterior_2')

  }


  async llenarFormulario() {
    await this.direcciones_anteriores_tab.click();
    await this.desde_1.fill('2017-05-30');
    await this.hasta_1.fill('2018-06-27');
    await this.tipo_via_anterior_1.selectOption('Carrera');
    await this.numero_principal_anterior_1.fill('71');
    await this.letra_principal_anterior_1.selectOption('B');
    await this.bis_anterior_1.check();
    await this.letra_bis_anterior_1.selectOption('A');
    await this.cuadrante_anterior_1.selectOption('ESTE');
    await this.numero_secundario_anterior_1.fill('5');
    await this.letra_secundaria_anterior_1.selectOption('A');
    await this.cuadrante_dos_anterior_1.selectOption('ESTE');
    await this.nro_anterior_1.fill('18');
    await this.complemento_anterior_1.fill('Primer Piso');
    await this.telefono_direccion_anterior_1_1.fill('1234567');
    await this.telefono_direccion_anterior_1_2.fill('7654321')
    await this.ciudad_direccion_anterior_1.fill('Bogotá')

    await this.desde_2.fill('2019-05-30');
    await this.hasta_2.fill('2021-06-27');
    await this.tipo_via_anterior_2.selectOption('Carrera');
    await this.numero_principal_anterior_2.fill('70');
    await this.letra_principal_anterior_2.selectOption('B');
    await this.bis_anterior_2.check();
    await this.letra_bis_anterior_2.selectOption('B');
    await this.cuadrante_anterior_2.selectOption('OESTE');
    await this.numero_secundario_anterior_2.fill('8');
    await this.letra_secundaria_anterior_2.selectOption('B');
    await this.cuadrante_dos_anterior_2.selectOption('NORTE');
    await this.nro_anterior_2.fill('71');
    await this.complemento_anterior_2.fill('Primer Piso');
    await this.telefono_direccion_anterior_2_1.fill('896521325');
    await this.telefono_direccion_anterior_2_2.fill('765431521');
    await this.ciudad_direccion_anterior_2.fill('Bogotá');

  } 

  async obtenerDireccionFormateadaAnterior1(): Promise<string> {
  const DireccionFormateadaAnterior1 = await this.direccion_completa_anterior_1.textContent();
  return DireccionFormateadaAnterior1?.trim() ?? '';
}
  async obtenerDireccionFormateadaAnterior2(): Promise<string> {
  const DireccionFormateadaAnterior2 = await this.direccion_completa_anterior_2.textContent();
  return DireccionFormateadaAnterior2?.trim() ?? '';
}

}