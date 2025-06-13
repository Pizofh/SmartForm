import { test, expect } from '@playwright/test';
import { DatosPersonalesPage } from '../pages/Recluta.page';
import { DireccionesAnterioresPage } from '../pages/DireccionesAnteriores.page';
import { DatosFamilaresPage } from '../pages/DatosFamiliares.page';
import { InformacionAcademicaPage } from '../pages/InformacionAcademica.page';
import { ReferenciasPersonalesPage } from '../pages/ReferenciasPersonales.page';
import { SectorDefensaPage } from '../pages/SectorDefensa.page';
import { BienesRentasPage } from '../pages/BienesRentas.page';
import { SituacionJuridicaPage } from '../pages/SituacionJuridica.page';
import { OtrosDatosPage } from '../pages/OtrosDatos.page';
import { ConfirmarPage } from '../pages/Confirmar.page';


test('Formulario: datos personales válidos', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/');

  //RECLUTA
  const datosPersonales = new DatosPersonalesPage(page);
  await datosPersonales.llenarFormulario();
  const direccionrecluta = await datosPersonales.obtenerDireccionFormateadaRecluta();
  expect(direccionrecluta).toBe('Carrera 69 C BIS A ESTE # 69 H ESTE 22, Segundo Piso');
 
//DIRECCIONES ANTERIORES
  const direccionesanteriores = new DireccionesAnterioresPage(page);
  await direccionesanteriores.llenarFormulario();
  const direccionanterior1 = await direccionesanteriores.obtenerDireccionFormateadaAnterior1();
  const direccionanterior2 = await direccionesanteriores.obtenerDireccionFormateadaAnterior2();
  expect(direccionanterior1).toBe('Carrera 71 B BIS A ESTE # 5 A ESTE 18, Primer Piso');
  expect(direccionanterior2).toBe('Carrera 70 B BIS B OESTE # 8 B NORTE 71, Primer Piso');

//DATOS FAMILIARES
  const datosfamiliares = new DatosFamilaresPage(page);
  await datosfamiliares.llenarFormulario();
  const direccionConyugue = await datosfamiliares.obtenerDireccionFormateadaConyugue();
  const direccionPadre = await datosfamiliares.obtenerDireccionFormateadaPadre();
  const direccionMadre = await datosfamiliares.obtenerDireccionFormateadaMadre();
  const direccionHermano = await datosfamiliares.obtenerDireccionFormateadaHermano();
  const direccionHermano1 = await datosfamiliares.obtenerDireccionFormateadaHermano1();
  const direccionHermano2 = await datosfamiliares.obtenerDireccionFormateadaHermano2();
  expect(direccionConyugue).toBe('Calle 167 A NORTE # 56 B OESTE 73, Torre 4 apto 4');
  expect(direccionPadre).toBe('Calle 50 H BIS F SUR # 89 J OESTE 789, Bosa');
  expect(direccionMadre).toBe('Anillo Vial 230 O Z NORTE # 566 P ESTE 200, Casa tercer piso');
  expect(direccionHermano).toBe('Calle 50 H BIS F SUR # 89 J OESTE 789, Bosa');
  expect(direccionHermano1).toBe('Calle 50 H BIS F SUR # 89 J OESTE 789, Bosa');
  expect(direccionHermano2).toBe('Calle 50 H BIS F SUR # 89 J OESTE 789, Bosa');
  
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

//SECTOR DEFENSA
  const SectorDefensa =new SectorDefensaPage(page);
  await SectorDefensa.llenarFormulario();

  const DireccionSectorDefensa1 = await SectorDefensa.obtenerDireccionFormateadaSectorDefensa1();
  const DireccionSectorDefensa2 = await SectorDefensa.obtenerDireccionFormateadaSectorDefensa2();
  expect(DireccionSectorDefensa1).toBe('Calle 123 G BIS A OESTE # 89 T SUR 101, complemento');
  expect(DireccionSectorDefensa2).toBe('Avenida 66 Q C NORTE # 55 N SUR 52, Complemento segundo');

//BIENES Y RENTAS
  const BienesRentas =new BienesRentasPage(page);
  await BienesRentas.llenarFormulario();
  const totalIngresos = await BienesRentas.obtenerTotalIngresos();
  expect(totalIngresos).toBe('$989.663.025');

//SITUACIÓN JURÍDICA
  const SituacionJuridica =new SituacionJuridicaPage(page);
  await SituacionJuridica.llenarFormulario();

//OTROS DATOS
  const OtrosDatos =new OtrosDatosPage(page);
  await OtrosDatos.llenarFormulario();
  const DireccionRecomendante = await OtrosDatos.obtenerDireccionFormateadaRecomendante();
  expect(DireccionRecomendante).toBe('Calle 23 B BIS C ESTE # 14 F NORTE 122, Tercer Piso Apartamento 232');

await page.click('button[type="submit"]');
await page.waitForURL('http://127.0.0.1:8000/exito/');
expect(page.url()).toBe('http://127.0.0.1:8000/exito/');
});
