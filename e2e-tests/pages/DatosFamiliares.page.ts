import { Page, Locator } from '@playwright/test';

export class DatosFamilaresPage {
  readonly page: Page;
  readonly tab: Locator;

//Datos Conyugue
  readonly DatosFamiliaresTab : Locator;
  readonly nombre_conyugue : Locator;
  readonly cedula_conyugue : Locator;
  readonly profesion_oficio_conyugue : Locator;
  readonly celular_conyugue : Locator;
  readonly tipo_via_conyugue : Locator;
  readonly numero_principal_conyugue : Locator;
  readonly letra_principal_conyugue: Locator;
  readonly bis_conyugue: Locator;
  readonly letra_bis_conyugue : Locator;
  readonly cuadrante_conyugue: Locator;
  readonly numero_secundario_conyugue : Locator;
  readonly letra_secundaria_conyugue: Locator;
  readonly cuadrante_dos_conyugue : Locator;
  readonly nro_conyugue : Locator;
  readonly complemento_conyugue : Locator;
  readonly direccion_formateada_conyugue : Locator;

//DATOS PADRE
  readonly nombre_padre : Locator;
  readonly vive_padre: Locator;
  readonly identificación_padre: Locator; 
  readonly telefono_padre : Locator;
  readonly oficio_profesion_padre : Locator;
  readonly tipo_via_padre: Locator;
  readonly numero_principal_padre : Locator;
  readonly letra_principal_padre: Locator;
  readonly bis_padre: Locator;
  readonly letra_bis_padre : Locator;
  readonly cuadrante_padre : Locator;
  readonly numero_secundario_padre: Locator;
  readonly letra_secundaria_padre : Locator;
  readonly cuadrante_dos_padre: Locator;
  readonly nro_padre : Locator;
  readonly complemento_padre: Locator;
  readonly direccion_formateada_padre : Locator;

//DATOS MADRE
  readonly nombre_madre: Locator;
  readonly vive_madre : Locator;
  readonly identificación_madre : Locator;
  readonly telefono_madre: Locator;
  readonly oficio_profesion_madre: Locator;
  readonly tipo_via_madre : Locator;
  readonly numero_principal_madre : Locator;
  readonly letra_principal_madre: Locator;
  readonly bis_madre: Locator;
  readonly letra_bis_madre : Locator;
  readonly cuadrante_madre: Locator;
  readonly numero_secundario_madre : Locator;
  readonly letra_secundaria_madre: Locator;
  readonly cuadrante_dos_madre: Locator;
  readonly nro_madre : Locator;
  readonly complemento_madre: Locator;
  readonly direccion_formateada_madre : Locator;

  
//DATOS HIJOS
  readonly nombre: Locator;
  readonly edad : Locator;
  readonly identificacion : Locator;
  readonly nombre_1: Locator;
  readonly edad_1 : Locator;
  readonly identificacion_1 : Locator;
  readonly agregar_hijo : Locator;
  readonly eliminar_hijo : Locator;

//DATOS HERMANOS
  readonly primer_apellido: Locator;
  readonly segundo_apellido: Locator;
  readonly primer_nombre: Locator;
  readonly segundo_nombre: Locator;
  readonly identificacion_hermano : Locator;
  readonly ocupacion_hermano :Locator;
  readonly celular_hermano: Locator;
  readonly agregar_hermano  :Locator;
  readonly primer_apellido_1: Locator;
  readonly segundo_apellido_1: Locator;
  readonly primer_nombre_1: Locator;
  readonly segundo_nombre_1: Locator;
  readonly identificacion_hermano_1 : Locator;
  readonly ocupacion_hermano_1 :Locator;
  readonly celular_hermano_1: Locator;
  readonly primer_apellido_2: Locator;
  readonly segundo_apellido_2: Locator;
  readonly primer_nombre_2: Locator;
  readonly segundo_nombre_2: Locator;
  readonly identificacion_hermano_2 : Locator;
  readonly ocupacion_hermano_2 :Locator;
  readonly celular_hermano_2: Locator;


  constructor(page: Page) {
    this.page = page;
    this.tab = page.locator('text=Datos Familiares');
    this.DatosFamiliaresTab=page.locator('#tab-datos-familiares');

  this.nombre_conyugue = page.locator('#id_DatosFamiliares-nombre_conyugue')
  this.cedula_conyugue = page.locator('#id_DatosFamiliares-cedula_conyugue')
  this.profesion_oficio_conyugue = page.locator('#id_DatosFamiliares-profesion_oficio_conyugue')
  this.celular_conyugue = page.locator('#id_DatosFamiliares-celular_conyugue')
  this.tipo_via_conyugue = page.locator('#id_DatosFamiliares-tipo_via_conyugue')
  this.numero_principal_conyugue = page.locator('#id_DatosFamiliares-numero_principal_conyugue')
  this.letra_principal_conyugue= page.locator('#id_DatosFamiliares-letra_principal_conyugue')
  this.bis_conyugue= page.locator('#id_DatosFamiliares-bis_conyugue')
  this.letra_bis_conyugue = page.locator('#id_DatosFamiliares-letra_bis_conyugue')
  this.cuadrante_conyugue= page.locator('#id_DatosFamiliares-cuadrante_conyugue')
  this.numero_secundario_conyugue = page.locator('#id_DatosFamiliares-numero_secundario_conyugue')
  this.letra_secundaria_conyugue= page.locator('#id_DatosFamiliares-letra_secundaria_conyugue')
  this.cuadrante_dos_conyugue = page.locator('#id_DatosFamiliares-cuadrante_dos_conyugue')
  this.nro_conyugue = page.locator('#id_DatosFamiliares-nro_conyugue')
  this.complemento_conyugue = page.locator('#id_DatosFamiliares-complemento_conyugue')
  this.direccion_formateada_conyugue = page.locator('#direccion-preview_conyugue')

//DATOS PADRE
  this.nombre_padre = page.locator('#id_DatosFamiliares-nombre_padre')
  this.vive_padre= page.locator('#id_DatosFamiliares-vive_padre')
  this.identificación_padre= page.locator('#id_DatosFamiliares-identificación_padre')
  this. telefono_padre = page.locator('#id_DatosFamiliares-telefono_padre')
  this.oficio_profesion_padre = page.locator('#id_DatosFamiliares-oficio_profesion_padre')
  this.tipo_via_padre= page.locator('#id_DatosFamiliares-tipo_via_padre')
  this.numero_principal_padre = page.locator('#id_DatosFamiliares-numero_principal_padre')
  this.letra_principal_padre= page.locator('#id_DatosFamiliares-letra_principal_padre')
  this.bis_padre= page.locator('#id_DatosFamiliares-bis_padre')
  this.letra_bis_padre = page.locator('#id_DatosFamiliares-letra_bis_padre')
  this.cuadrante_padre = page.locator('#id_DatosFamiliares-cuadrante_padre')
  this.numero_secundario_padre= page.locator('#id_DatosFamiliares-numero_secundario_padre')
  this.letra_secundaria_padre = page.locator('#id_DatosFamiliares-letra_secundaria_padre')
  this.cuadrante_dos_padre= page.locator('#id_DatosFamiliares-cuadrante_dos_padre')
  this.nro_padre = page.locator('#id_DatosFamiliares-nro_padre')
  this.complemento_padre= page.locator('#id_DatosFamiliares-complemento_padre')
  this.direccion_formateada_padre = page.locator('#direccion-preview_padre')  

//DATOS MADRE
  this.nombre_madre = page.locator('#id_DatosFamiliares-nombre_madre')
  this.vive_madre = page.locator('#id_DatosFamiliares-vive_madre')
  this.identificación_madre = page.locator('#id_DatosFamiliares-identificación_madre')
  this.telefono_madre = page.locator('#id_DatosFamiliares-telefono_madre')
  this.oficio_profesion_madre = page.locator('#id_DatosFamiliares-oficio_profesion_madre')
  this.tipo_via_madre = page.locator('#id_DatosFamiliares-tipo_via_madre')
  this.numero_principal_madre = page.locator('#id_DatosFamiliares-numero_principal_madre')
  this.letra_principal_madre = page.locator('#id_DatosFamiliares-letra_principal_madre')
  this.bis_madre = page.locator('#id_DatosFamiliares-bis_madre')
  this.letra_bis_madre = page.locator('#id_DatosFamiliares-letra_bis_madre')
  this.cuadrante_madre = page.locator('#id_DatosFamiliares-cuadrante_madre')
  this.numero_secundario_madre = page.locator('#id_DatosFamiliares-numero_secundario_madre')
  this.letra_secundaria_madre = page.locator('#id_DatosFamiliares-letra_secundaria_madre')
  this.cuadrante_dos_madre = page.locator('#id_DatosFamiliares-cuadrante_dos_madre')
  this.nro_madre = page.locator('#id_DatosFamiliares-nro_madre')
  this.complemento_madre = page.locator('#id_DatosFamiliares-complemento_madre')
  this.direccion_formateada_madre = page.locator('#direccion-preview_madre')

  //DATOS HIJOS
  this.nombre = page.locator('#id_hijos-0-nombre');
  this.edad = page.locator('#id_hijos-0-edad');
  this.identificacion = page.locator('#id_hijos-0-identificacion');
  this.agregar_hijo = page.locator('#add-hijo');
  this.eliminar_hijo = page.locator('//*[@id="formset-hijos"]/div[3]/div/button');
  this.nombre_1 = page.locator('#id_hijos-1-nombre')
  this.edad_1 = page.locator('#id_hijos-1-edad')
  this.identificacion_1 =page.locator('#id_hijos-1-identificacion')

  //DATOS HERMANOS
  this.primer_apellido =page.locator('#id_hermanos-0-primer_apellido_hermano');
  this.segundo_apellido =page.locator('#id_hermanos-0-segundo_apellido_hermano');
  this.primer_nombre =page.locator('#id_hermanos-0-primer_nombre_hermano');
  this.segundo_nombre =page.locator('#id_hermanos-0-segundo_nombre_hermano');
  this.identificacion_hermano =page.locator('#id_hermanos-0-identificacion_hermano');
  this.ocupacion_hermano =page.locator('#id_hermanos-0-ocupacion_hermano');
  this.celular_hermano =page.locator('#id_hermanos-0-celular_hermano');
  this.agregar_hermano = page.locator('#add-hermano');
  this.primer_apellido_1 =page.locator('#id_hermanos-1-primer_apellido_hermano');
  this.segundo_apellido_1=page.locator('#id_hermanos-1-segundo_apellido_hermano');
  this.primer_nombre_1 =page.locator('#id_hermanos-1-primer_nombre_hermano');
  this.segundo_nombre_1 =page.locator('#id_hermanos-1-segundo_nombre_hermano');
  this.identificacion_hermano_1 =page.locator('#id_hermanos-1-identificacion_hermano');
  this.ocupacion_hermano_1 =page.locator('#id_hermanos-1-ocupacion_hermano');
  this.celular_hermano_1 =page.locator('#id_hermanos-1-celular_hermano');
  this.primer_apellido_2 =page.locator('#id_hermanos-2-primer_apellido_hermano');
  this.segundo_apellido_2=page.locator('#id_hermanos-2-segundo_apellido_hermano');
  this.primer_nombre_2 =page.locator('#id_hermanos-2-primer_nombre_hermano');
  this.segundo_nombre_2 =page.locator('#id_hermanos-2-segundo_nombre_hermano');
  this.identificacion_hermano_2 =page.locator('#id_hermanos-2-identificacion_hermano');
  this.ocupacion_hermano_2 =page.locator('#id_hermanos-2-ocupacion_hermano');
  this.celular_hermano_2 =page.locator('#id_hermanos-2-celular_hermano');
  }


  async llenarFormulario() {

  await this.DatosFamiliaresTab.click();
  await this.nombre_conyugue.fill('María José Rodriguez Tribiño');
  await this.cedula_conyugue.fill('1001346476');
  await this.profesion_oficio_conyugue.fill('Veterinaria');
  await this.celular_conyugue.fill('3153135284');
  await this.tipo_via_conyugue.selectOption('Calle');
  await this.numero_principal_conyugue.fill('167');
  await this.letra_principal_conyugue.selectOption('A');
  await this.bis_conyugue.uncheck();
  await this.letra_bis_conyugue
  await this.cuadrante_conyugue.selectOption('NORTE');
  await this.numero_secundario_conyugue.fill('56');
  await this.letra_secundaria_conyugue.selectOption('B');
  await this.cuadrante_dos_conyugue.selectOption('OESTE');
  await this.nro_conyugue.fill('73');
  await this.complemento_conyugue.fill('Torre 4 apto 4');
  await this.direccion_formateada_conyugue

//DATOS PADRE
  await this.nombre_padre.fill('Johny Alexander Garnica Jimenez');
  await this.vive_padre.selectOption('Sí');
  await this.identificación_padre.fill('7173397');
  await this.telefono_padre.fill('3017337009');
  await this.oficio_profesion_padre.fill('Independiente');
  await this.tipo_via_padre.selectOption('Calle');
  await this.numero_principal_padre.fill('50');
  await this.letra_principal_padre.selectOption('H');
  await this.bis_padre.check();
  await this.letra_bis_padre.selectOption('F');
  await this.cuadrante_padre.selectOption('SUR');
  await this.numero_secundario_padre.fill('89');
  await this.letra_secundaria_padre.selectOption('J');
  await this.cuadrante_dos_padre.selectOption('OESTE');
  await this.nro_padre.fill('789');
  await this.complemento_padre.fill('Bosa');
  await this.direccion_formateada_padre

//DATOS MADRE
  await this.nombre_madre.fill('Milena Astrid Sandoval Villamil');
  await this.vive_madre.selectOption('Sí');
  await this.identificación_madre.fill('40046564');
  await this.telefono_madre.fill('3134690645');
  await this.oficio_profesion_madre.fill('Abogada');
  await this.tipo_via_madre.selectOption('Anillo Vial');
  await this.numero_principal_madre.fill('230');
  await this.letra_principal_madre.selectOption('O');
  await this.bis_madre.uncheck();
  await this.letra_bis_madre.selectOption('Z'); 
  await this.cuadrante_madre.selectOption('NORTE');
  await this.numero_secundario_madre.fill('566');
  await this.letra_secundaria_madre.selectOption('P');
  await this.cuadrante_dos_madre.selectOption('ESTE');
  await this.nro_madre.fill('200');
  await this.complemento_madre.fill('Casa tercer piso');
  await this.direccion_formateada_madre

//DATOS HIJOS
  await this.nombre.fill('Rocko Garnica');
  await this.edad.fill('9');
  await this.identificacion.fill('1351386');
  await this.agregar_hijo.click();
  await this.agregar_hijo.click();
  await this.nombre_1.fill('Chispun');
  await this.edad_1.fill('2');
  await this.identificacion_1.fill('19128731');
  await this.eliminar_hijo.click();

//DATOS HERMANOS

  await this.primer_apellido.fill('Garnica');
  await this.segundo_apellido.fill('Sandoval');
  await this.primer_nombre.fill('Melany');
  await this.segundo_nombre
  await this.identificacion_hermano.fill('53513525');
  await this.ocupacion_hermano.fill('Estudiante');
  await this.celular_hermano.fill('3136546548');
  await this.agregar_hermano.click();
  await this.agregar_hermano.click();
  await this.agregar_hermano.click();
  await this.primer_apellido_1.fill('Garnicaasdasd');
  await this.segundo_apellido_1.fill('Sandovaldsadas');
  await this.primer_nombre_1.fill('Melanyasdasda');
  await this.segundo_nombre_1
  await this.identificacion_hermano_1.fill('535131561');
  await this.ocupacion_hermano_1.fill('Estudianteeee');
  await this.celular_hermano_1.fill('3136546515');
  await this.primer_apellido_2.fill('abecede');
  await this.segundo_apellido_2.fill('efege');
  await this.primer_nombre_2.fill('hachei');
  await this.segundo_nombre_2.fill('jotaca');
  await this.identificacion_hermano_2.fill('77766655');
  await this.ocupacion_hermano_2.fill('Trabajador');
  await this.celular_hermano_2.fill('3136546525');
  } 

  async logDireccionesFormateadasFamilia() {

  const DireccionFormateadaConyugue = await this.direccion_formateada_conyugue.textContent();
  console.log('📍 Dirección Conyugue generada:', DireccionFormateadaConyugue);
  const DireccionFormateadaPadre = await this.direccion_formateada_padre.textContent();
  console.log('📍 Dirección Padre generada:', DireccionFormateadaPadre);
  const DireccionFormateadaMadre = await this.direccion_formateada_madre.textContent();
  console.log('📍 Dirección Madre generada:', DireccionFormateadaMadre);
  }

}