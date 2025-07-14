import { Page, Locator } from '@playwright/test';

export class BienesRentasPage {
  readonly page: Page;
  readonly tab: Locator;
  readonly bienes_rentas_tab : Locator; 

//Total de Ingresos Último Año Gravable
  readonly salarios_y_demas_ingresos_laborales:Locator
  readonly cesantías_e_intereses_de_cesantías :Locator;
  readonly gastos_de_representación:Locator;
  readonly arriendos:Locator;
  readonly honorarios:Locator;
  readonly otros_ingresos_y_rentas:Locator;
  readonly total_ingresos : Locator;

//Las cuentas corrientes, de ahorros o tarjeta de crédito que poseo en Colombia y el Exterior son:

  readonly entidad_financiera_1 : Locator; 
  readonly tipo_de_cuenta_1:Locator
  readonly numero_de_cuenta_1 :Locator;
  readonly entidad_financiera_2 : Locator; 
  readonly tipo_de_cuenta_2:Locator
  readonly numero_de_cuenta_2 :Locator;


//Mis bienes patrimoniales son los siguientes:
  readonly tipo_bien_1 : Locator;
  readonly ubicacion_bien_1 :Locator;
  readonly identificacion_bien_1 :Locator;
  readonly avaluo_comercial_bien_1 :Locator;
  
  readonly tipo_bien_2 : Locator;
  readonly ubicacion_bien_2 :Locator;
  readonly identificacion_bien_2 :Locator;
  readonly avaluo_comercial_bien_2 :Locator;


//Mis Obligaciones vigentes a la fecha:
  readonly entidad_o_persona_obligacion_1 : Locator;
  readonly concepto_obligacion_1 : Locator;
  readonly valor_1 : Locator;

  readonly entidad_o_persona_obligacion_2 : Locator;
  readonly concepto_obligacion_2 : Locator;
  readonly valor_2 : Locator;



//PARTICIPACION EN ORGANIZACIONES, CORPORACIONES, SOCIEDADES, ASOCIACIONES, ONG's u OTROS.

  readonly entidad_o_institucion_1 :Locator;
  readonly calidad_de_miembro_1 : Locator;

  readonly entidad_o_institucion_2 :Locator;
  readonly calidad_de_miembro_2 : Locator;



//ACTIVIDAD ECONÓMICA PRIVADA DEL ASPIRANTE
    
  readonly empresa_1 : Locator; 
  readonly calidad_de_miembro_AEP_1: Locator;

  readonly empresa_2 : Locator;
  readonly calidad_de_miembro_AEP_2: Locator;





constructor(page: Page) {
    this.page = page;
    this.tab = page.locator('text=Bienes Rentas');

//Total de Ingresos Último Año Gravable
    this.bienes_rentas_tab = page.locator('#formTabs > li:nth-child(6) > button');
    this.salarios_y_demas_ingresos_laborales =page.locator('#id_BienesRentasAEP-salarios_y_demas_ingresos_laborales');
    this.cesantías_e_intereses_de_cesantías = page.locator('#id_BienesRentasAEP-cesantías_e_intereses_de_cesantías');
    this.gastos_de_representación = page.locator('#id_BienesRentasAEP-gastos_de_representación');
    this.arriendos = page.locator('#id_BienesRentasAEP-arriendos');
    this.honorarios = page.locator('#id_BienesRentasAEP-honorarios');
    this.otros_ingresos_y_rentas = page.locator('#id_BienesRentasAEP-otros_ingresos_y_rentas');
    this.total_ingresos = page.locator('#id_BienesRentasAEP-total_ingresos');

//Las cuentas corrientes, de ahorros o tarjeta de crédito que poseo en Colombia y el Exterior son:

  this.entidad_financiera_1 = page.locator('#id_BienesRentasAEP-entidad_financiera_1');
  this.tipo_de_cuenta_1 = page.locator('#id_BienesRentasAEP-tipo_de_cuenta_1');
  this.numero_de_cuenta_1 = page.locator('#id_BienesRentasAEP-numero_de_cuenta_1');

  this.entidad_financiera_2 = page.locator('#id_BienesRentasAEP-entidad_financiera_2'); 
  this.tipo_de_cuenta_2 = page.locator('#id_BienesRentasAEP-tipo_de_cuenta_2');
  this.numero_de_cuenta_2 = page.locator('#id_BienesRentasAEP-numero_de_cuenta_2');



//Mis bienes patrimoniales son los siguientes:
  this.tipo_bien_1 = page.locator('#id_BienesRentasAEP-tipo_bien_1');
  this.ubicacion_bien_1 = page.locator('#id_BienesRentasAEP-ubicacion_bien_1');
  this.identificacion_bien_1 = page.locator('#id_BienesRentasAEP-identificacion_bien_1');
  this.avaluo_comercial_bien_1 = page.locator('#id_BienesRentasAEP-avaluo_comercial_bien_1');

  this.tipo_bien_2 = page.locator('#id_BienesRentasAEP-tipo_bien_2');
  this.ubicacion_bien_2 = page.locator('#id_BienesRentasAEP-ubicacion_bien_2');
  this.identificacion_bien_2 = page.locator('#id_BienesRentasAEP-identificacion_bien_2');
  this.avaluo_comercial_bien_2 = page.locator('#id_BienesRentasAEP-avaluo_comercial_bien_2');


//Mis Obligaciones vigentes a la fecha:
  this.entidad_o_persona_obligacion_1 = page.locator('#id_BienesRentasAEP-entidad_o_persona_obligacion_1');
  this.concepto_obligacion_1 = page.locator('#id_BienesRentasAEP-concepto_obligacion_1');
  this.valor_1 = page.locator('#id_BienesRentasAEP-valor_1');

  this.entidad_o_persona_obligacion_2 = page.locator('#id_BienesRentasAEP-entidad_o_persona_obligacion_2');
  this.concepto_obligacion_2 = page.locator('#id_BienesRentasAEP-concepto_obligacion_2');
  this.valor_2 = page.locator('#id_BienesRentasAEP-valor_2');


//PARTICIPACION EN ORGANIZACIONES, CORPORACIONES, SOCIEDADES, ASOCIACIONES, ONG's u OTROS.

  this.entidad_o_institucion_1 = page.locator('#id_BienesRentasAEP-entidad_o_institucion_1');
  this.calidad_de_miembro_1 = page.locator('#id_BienesRentasAEP-calidad_de_miembro_1');

  this.entidad_o_institucion_2 = page.locator('#id_BienesRentasAEP-entidad_o_institucion_2');
  this.calidad_de_miembro_2 = page.locator('#id_BienesRentasAEP-calidad_de_miembro_2');



  //ACTIVIDAD ECONÓMICA PRIVADA DEL ASPIRANTE
    
  this.empresa_1 = page.locator('#id_BienesRentasAEP-empresa_1');
  this.calidad_de_miembro_AEP_1 = page.locator('#id_BienesRentasAEP-calidad_de_miembro_AEP_1');

  this.empresa_2 = page.locator('#id_BienesRentasAEP-empresa_2');
  this.calidad_de_miembro_AEP_2 = page.locator('#id_BienesRentasAEP-calidad_de_miembro_AEP_2');


  }


  async llenarFormulario() {

    await this.bienes_rentas_tab.click();

  //Total de Ingresos Último Año Gravable
    await this.salarios_y_demas_ingresos_laborales.fill('123456');
    await this.cesantías_e_intereses_de_cesantías.fill('987654321');
    await this.gastos_de_representación.fill('741258');
    await this.arriendos.fill('654987');
    await this.honorarios.fill('365214');
    await this.otros_ingresos_y_rentas.fill('123789');
    await this.total_ingresos 

//Las cuentas corrientes, de ahorros o tarjeta de crédito que poseo en Colombia y el Exterior son:

  await this.entidad_financiera_1.fill('Entidad bancaria 1');
  await this.tipo_de_cuenta_1.fill('Ahorros');
  await this.numero_de_cuenta_1.fill('123456789123457');

  await this.entidad_financiera_2.fill('Entidad bancaria 2');
  await this.tipo_de_cuenta_2.fill('Ahorros');
  await this.numero_de_cuenta_2.fill('987654321963852');


//Mis bienes patrimoniales son los siguientes:

  await this.tipo_bien_1.fill('Carro');
  await this.ubicacion_bien_1.fill('Tunja');
  await this.identificacion_bien_1.fill('identificaciondecarro');
  await this.avaluo_comercial_bien_1.fill('123456789');

  await this.tipo_bien_2.fill('casa');
  await this.ubicacion_bien_2.fill('Yopal');
  await this.identificacion_bien_2.fill('123456789'); 
  await this.avaluo_comercial_bien_2.fill('74125368');



//Mis Obligaciones vigentes a la fecha:
  await this.entidad_o_persona_obligacion_1.fill('Obligación 1');
  await this.concepto_obligacion_1.fill('Esta es la razón para esta obligación 1');
  await this.valor_1.fill('111111');

  await this.entidad_o_persona_obligacion_2.fill('Obligación 2');
  await this.concepto_obligacion_2.fill('Esta es la razón para esta obligación 2');
  await this.valor_2.fill('222222');


//PARTICIPACION EN ORGANIZACIONES, CORPORACIONES, SOCIEDADES, ASOCIACIONES, ONG's u OTROS.

  await this.entidad_o_institucion_1.fill('Organización');
  await this.calidad_de_miembro_1.fill('Miembro 1');

  await this.entidad_o_institucion_2.fill('Corporación');
  await this.calidad_de_miembro_2.fill('Gerente');


  //ACTIVIDAD ECONÓMICA PRIVADA DEL ASPIRANTE
    
  await this.empresa_1.fill('Empresa 1');
  await this.calidad_de_miembro_AEP_1.fill('Presidente'); 

  await this.empresa_2.fill('Empresa 2');
  await this.calidad_de_miembro_AEP_2.fill('Afiliado'); 

  } 

  async obtenerTotalIngresos(): Promise<string> {
  const totalsuma = await this.total_ingresos.inputValue();
  return totalsuma.trim();
}
}