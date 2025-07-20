import { test, expect } from '@playwright/test';

test('Formulario: error al enviar campos vacíos', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/');

  // Simula el envío sin llenar ningún campo
  await page.click('button[type="submit"]');

  // Verifica que se muestren errores en los campos obligatorios
  const errors = await page.locator('div.invalid-feedback strong');
  await expect(errors).toHaveCount(34)

  // Verifica que no redirige a la página de éxito
  expect(page.url()).not.toContain('/exito/');
});
