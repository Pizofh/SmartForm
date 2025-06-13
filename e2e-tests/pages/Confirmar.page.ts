import { Page, Locator } from '@playwright/test';

export class ConfirmarPage {
  readonly page: Page;
  readonly tab: Locator;

    readonly Confirmar_tab : Locator;
    readonly captcha : Locator;


  constructor(page: Page) {
    this.page = page;
    this.tab = page.locator('text=Confirmar');

    this.Confirmar_tab=page.locator('#formTabs > li:nth-child(10) > button');
    this.captcha =page.locator('#recaptcha-anchor > div.recaptcha-checkbox-border')
  }

  async llenarFormulario() {
    await this.Confirmar_tab.click();
    await this.captcha.click();


  } 
}

