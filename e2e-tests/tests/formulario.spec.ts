import { test, expect } from '@playwright/test';
import { DatosPersonalesPage } from '../pages/Recluta.page';
import { DireccionesAnterioresPage } from '../pages/DireccionesAnteriores.page';
import { DatosFamilaresPage } from '../pages/DatosFamiliares.page';

test('Formulario: datos personales válidos', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/');

  const datosPersonales = new DatosPersonalesPage(page);
  await datosPersonales.llenarFormulario();
  await datosPersonales.logDireccionFormateadaRecluta();

  const direccionesanteiores = new DireccionesAnterioresPage(page);
  await direccionesanteiores.llenarFormulario();
  await direccionesanteiores.logDireccionesFormateadasAnteriores();

  const datosfamiliares = new DatosFamilaresPage(page);
  await datosfamiliares.llenarFormulario();
  await datosfamiliares.logDireccionesFormateadasFamilia()


  // Aquí puedes seguir con las otras secciones (Direcciones, Familiares, etc.)
});
