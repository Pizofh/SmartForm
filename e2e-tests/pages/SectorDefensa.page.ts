import { Page, Locator } from '@playwright/test';

export class SectorDefensaPage {
  readonly page: Page;
  readonly tab: Locator;
  readonly sector_defensa_tab : Locator;
  readonly nombresyapellidos_sd_1 : Locator;
  readonly cargo_sd_1: Locator;
  readonly entidad_sd_1: Locator;
  readonly unidad_militar_sd_1 : Locator;
  readonly celular_sd_1: Locator;
  readonly tipo_via_sd_1 : Locator;
  readonly numero_principal_sd_1 : Locator;
  readonly letra_principal_sd_1: Locator;
  readonly bis_sd_1 : Locator;
  readonly letra_bis_sd_1: Locator;
  readonly cuadrante_sd_1: Locator;
  readonly numero_secundario_sd_1: Locator;
  readonly letra_secundaria_sd_1: Locator;
  readonly cuadrante_dos_sd_1: Locator;
  readonly nro_sd_1: Locator;
  readonly complemento_sd_1: Locator;
  readonly direccion_formateada_sd_1: Locator;

  readonly nombresyapellidos_sd_2 : Locator;
  readonly cargo_sd_2: Locator;
  readonly entidad_sd_2: Locator;
  readonly unidad_militar_sd_2 : Locator;
  readonly celular_sd_2: Locator;
  readonly tipo_via_sd_2 : Locator;
  readonly numero_principal_sd_2 : Locator;
  readonly letra_principal_sd_2: Locator;
  readonly bis_sd_2 : Locator;
  readonly letra_bis_sd_2: Locator;
  readonly cuadrante_sd_2: Locator;
  readonly numero_secundario_sd_2: Locator;
  readonly letra_secundaria_sd_2: Locator;
  readonly cuadrante_dos_sd_2: Locator;
  readonly nro_sd_2: Locator;
  readonly complemento_sd_2: Locator;
  readonly direccion_formateada_sd_2: Locator;

  constructor(page: Page) {
    this.page = page;
    this.tab = page.locator('text=Datos Personales');

    this.sector_defensa_tab = page.locator('#formTabs > li:nth-child(5) > button');
    this.nombresyapellidos_sd_1 = page.locator('#id_SectorDefensa-nombresyapellidos_sd_1');
    this.cargo_sd_1 = page.locator('#id_SectorDefensa-cargo_sd_1');
    this.entidad_sd_1 = page.locator('#id_SectorDefensa-entidad_sd_1');
    this.unidad_militar_sd_1  = page.locator('#id_SectorDefensa-unidad_militar_sd_1');
    this.celular_sd_1 = page.locator('#id_SectorDefensa-celular_sd_1');
    this.tipo_via_sd_1 = page.locator('#id_SectorDefensa-tipo_via_sd_1');
    this.numero_principal_sd_1 = page.locator('#id_SectorDefensa-numero_principal_sd_1');
    this.letra_principal_sd_1 = page.locator('#id_SectorDefensa-letra_principal_sd_1');
    this.bis_sd_1 = page.locator('#id_SectorDefensa-bis_sd_1');
    this.letra_bis_sd_1 = page.locator('#id_SectorDefensa-letra_bis_sd_1');
    this.cuadrante_sd_1 = page.locator('#id_SectorDefensa-cuadrante_sd_1');
    this.numero_secundario_sd_1 = page.locator('#id_SectorDefensa-numero_secundario_sd_1');
    this.letra_secundaria_sd_1 = page.locator('#id_SectorDefensa-letra_secundaria_sd_1');
    this.cuadrante_dos_sd_1 = page.locator('#id_SectorDefensa-cuadrante_dos_sd_1');
    this.nro_sd_1 = page.locator('#id_SectorDefensa-nro_sd_1');
    this.complemento_sd_1 = page.locator('#id_SectorDefensa-complemento_sd_1');
    this.direccion_formateada_sd_1 = page.locator('#direccion-preview_sd_1');

    this.nombresyapellidos_sd_2 = page.locator('#id_SectorDefensa-nombresyapellidos_sd_2');
    this.cargo_sd_2 = page.locator('#id_SectorDefensa-cargo_sd_2');
    this.entidad_sd_2 = page.locator('#id_SectorDefensa-entidad_sd_2');
    this.unidad_militar_sd_2  = page.locator('#id_SectorDefensa-unidad_militar_sd_2');
    this.celular_sd_2 = page.locator('#id_SectorDefensa-celular_sd_2');
    this.tipo_via_sd_2 = page.locator('#id_SectorDefensa-tipo_via_sd_2');
    this.numero_principal_sd_2 = page.locator('#id_SectorDefensa-numero_principal_sd_2');
    this.letra_principal_sd_2 = page.locator('#id_SectorDefensa-letra_principal_sd_2');
    this.bis_sd_2 = page.locator('#id_SectorDefensa-bis_sd_2');
    this.letra_bis_sd_2 = page.locator('#id_SectorDefensa-letra_bis_sd_2');
    this.cuadrante_sd_2 = page.locator('#id_SectorDefensa-cuadrante_sd_2');
    this.numero_secundario_sd_2 = page.locator('#id_SectorDefensa-numero_secundario_sd_2');
    this.letra_secundaria_sd_2 = page.locator('#id_SectorDefensa-letra_secundaria_sd_2');
    this.cuadrante_dos_sd_2 = page.locator('#id_SectorDefensa-cuadrante_dos_sd_2');
    this.nro_sd_2 = page.locator('#id_SectorDefensa-nro_sd_2');
    this.complemento_sd_2 = page.locator('#id_SectorDefensa-complemento_sd_2');
    this.direccion_formateada_sd_2 = page.locator('#direccion-preview_sd_2');

  }


  async llenarFormulario() {
 
    await this.sector_defensa_tab.click();

    await this.nombresyapellidos_sd_1.fill('nombre generico punto com'); 
    await this.cargo_sd_1.fill('cargo 1');
    await this.entidad_sd_1.fill('entidad 1');
    await this.unidad_militar_sd_1.fill('unidad militar 1');
    await this.celular_sd_1.fill('3219876514');
    await this.tipo_via_sd_1.selectOption('Calle');
    await this.numero_principal_sd_1.fill('123');
    await this.letra_principal_sd_1.selectOption('G');
    await this.bis_sd_1.check();
    await this.letra_bis_sd_1.selectOption('A');
    await this.cuadrante_sd_1.selectOption('OESTE');
    await this.numero_secundario_sd_1.fill('89');
    await this.letra_secundaria_sd_1.selectOption('T');
    await this.cuadrante_dos_sd_1.selectOption('SUR');
    await this.nro_sd_1.fill('101');
    await this.complemento_sd_1.fill('complemento');

    await this.nombresyapellidos_sd_2.fill('nombre segundo'); 
    await this.cargo_sd_2.fill('cargo segundo');
    await this.entidad_sd_2.fill('entidad numero dos');
    await this.unidad_militar_sd_2.fill('unidad militar numero dos');
    await this.celular_sd_2.fill('3219634185');
    await this.tipo_via_sd_2.selectOption('Avenida');
    await this.numero_principal_sd_2.fill('66');
    await this.letra_principal_sd_2.selectOption('Q');
    await this.bis_sd_2.uncheck();
    await this.letra_bis_sd_2.selectOption('C');
    await this.cuadrante_sd_2.selectOption('NORTE');
    await this.numero_secundario_sd_2.fill('55');
    await this.letra_secundaria_sd_2.selectOption('N');
    await this.cuadrante_dos_sd_2.selectOption('SUR');
    await this.nro_sd_2.fill('52');
    await this.complemento_sd_2.fill('Complemento segundo');


  } 


  async obtenerDireccionFormateadaSectorDefensa1(): Promise<string> {
  const DireccionFormateadaSD1 = await this.direccion_formateada_sd_1.textContent();
  return DireccionFormateadaSD1?.trim() ?? '';

}

  async obtenerDireccionFormateadaSectorDefensa2(): Promise<string> {
  const DireccionFormateadaSD2 = await this.direccion_formateada_sd_2.textContent();
  return DireccionFormateadaSD2?.trim() ?? '';

}
}