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


test('Formulario: datos personales válidos', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/');

  const datosPersonales = new DatosPersonalesPage(page);
  await datosPersonales.llenarFormulario();
  await datosPersonales.logDireccionFormateadaRecluta();

  const direccionesanteriores = new DireccionesAnterioresPage(page);
  await direccionesanteriores.llenarFormulario();
  await direccionesanteriores.logDireccionesFormateadasAnteriores();

  const datosfamiliares = new DatosFamilaresPage(page);
  await datosfamiliares.llenarFormulario();
  await datosfamiliares.logDireccionesFormateadasFamilia()

  const InformacionAcademica = new InformacionAcademicaPage(page);
  await InformacionAcademica.llenarFormulario();

  const ReferenciasPersonales =new ReferenciasPersonalesPage(page);
  await ReferenciasPersonales.llenarFormulario();
  await ReferenciasPersonales.logDireccionFormateadaReferencias();

  const SectorDefensa =new SectorDefensaPage(page);
  await SectorDefensa.llenarFormulario();
  await SectorDefensa.logDireccionFormateadaSectorDefensa();

  const BienesRentas =new BienesRentasPage(page);
  await BienesRentas.llenarFormulario();

  const SituacionJuridica =new SituacionJuridicaPage(page);
  await SituacionJuridica.llenarFormulario();

  const OtrosDatos =new OtrosDatosPage(page);
  await OtrosDatos.llenarFormulario();
  await OtrosDatos.logDireccionFormateadaOtrosDatos();
});
