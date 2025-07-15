import { test, expect } from '@playwright/test';
import { DatosPersonalesPage } from '../pages/Recluta.page';
import { DatosFamilaresPage } from '../pages/DatosFamiliares.page';
import { InformacionAcademicaPage } from '../pages/InformacionAcademica.page';
import { ReferenciasPersonalesPage } from '../pages/ReferenciasPersonales.page';
import { BienesRentasPage } from '../pages/BienesRentas.page';
import { SituacionJuridicaPage } from '../pages/SituacionJuridica.page';


test('Formulario: datos personales válidos', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/');

  //RECLUTA
  const datosPersonales = new DatosPersonalesPage(page);
  await datosPersonales.llenarFormulario();
  const direccionrecluta = await datosPersonales.obtenerDireccionFormateadaRecluta();
  expect(direccionrecluta).toBe('Carrera 69 C BIS A ESTE # 69 H ESTE 22, Segundo Piso');
 


//DATOS FAMILIARES
  const datosfamiliares = new DatosFamilaresPage(page);
  await datosfamiliares.llenarFormulario();
  const direccionConyugue = await datosfamiliares.obtenerDireccionFormateadaConyugue();
  const direccionPadre = await datosfamiliares.obtenerDireccionFormateadaPadre();
  const direccionMadre = await datosfamiliares.obtenerDireccionFormateadaMadre();


const direccionHermano = await datosfamiliares.getDireccionHermano(0);
const direccionHermano1 = await datosfamiliares.getDireccionHermano(1);
const direccionHermano2 = await datosfamiliares.getDireccionHermano(2);



  expect(direccionConyugue).toBe('Calle 167 A NORTE # 56 B OESTE 73, Torre 4 apto 4');
  expect(direccionPadre).toBe('Calle 50 H BIS F SUR # 89 J OESTE 789, Bosa');
  expect(direccionMadre).toBe('Anillo Vial 230 O Z NORTE # 566 P ESTE 200, Casa tercer piso');
  expect(direccionHermano).toBe('Calle 50 H BIS F NORTE # 89 P ESTE 79, Bosa');
  expect(direccionHermano1).toBe('Calle 50 H BIS F SUR # 89 J OESTE 789, Bosa');
  expect(direccionHermano2).toBe('Carrera 123 H BIS F SUR # 89 J OESTE 789, Suba');

  
//INFORMACIÓN ACADÉMICA
  const InformacionAcademica = new InformacionAcademicaPage(page);
  await InformacionAcademica.llenarFormulario();


//REFERENCIAS PERSONALES
  const ReferenciasPersonales =new ReferenciasPersonalesPage(page);
  await ReferenciasPersonales.llenarFormulario();
  const DireccionReferencia1 = await ReferenciasPersonales.obtenerDireccionFormateadaReferencia1();
  const DireccionReferencia2 = await ReferenciasPersonales.obtenerDireccionFormateadaReferencia2();
  const DireccionReferencia3 = await ReferenciasPersonales.obtenerDireccionFormateadaReferencia3();
  expect(DireccionReferencia1).toBe('Calle 12 B BIS A OESTE # 45 H OESTE 456, APTO 987');
  expect(DireccionReferencia2).toBe('Carrera 56 H NORTE # 23 L SUR 457, SEGUNDO PISO');
  expect(DireccionReferencia3).toBe('Avenida 89 G BIS Y SUR # 56 Q ESTE 85, APARTAMENTO OOOO OOOO');


//BIENES Y RENTAS
  const BienesRentas =new BienesRentasPage(page);
  await BienesRentas.llenarFormulario();
  const totalIngresos = await BienesRentas.obtenerTotalIngresos();
  expect(totalIngresos).toBe('$989.663.025');

//SITUACIÓN JURÍDICA
  const SituacionJuridica =new SituacionJuridicaPage(page);
  await SituacionJuridica.llenarFormulario();

await page.click('button[type="submit"]');
await page.waitForURL('http://127.0.0.1:8000/exito/');
expect(page.url()).toBe('http://127.0.0.1:8000/exito/');

});
