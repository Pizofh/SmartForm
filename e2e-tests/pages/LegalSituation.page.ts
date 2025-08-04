import { Page, Locator } from '@playwright/test';

export class LegalSituationPage {
  readonly page: Page;
  readonly tab: Locator;

  readonly legal_situation_tab : Locator;
  readonly process_date_1  : Locator;
  readonly investigation_type_1  : Locator;
  readonly cause_1 : Locator;
  readonly authority_1  : Locator;
  readonly process_state_1  : Locator;
  readonly responsible_1  : Locator;

  readonly process_date_2  : Locator;
  readonly investigation_type_2  : Locator;
  readonly cause_2 : Locator;
  readonly authority_2  : Locator;
  readonly process_state_2 : Locator;
  readonly responsible_2 : Locator;



constructor(page: Page) {
  this.page = page;


  // Legal Situation Tab
this.tab = page.locator('text=Legal Situation');
this.legal_situation_tab = page.locator('#formTabs > li:nth-child(5) > button');

// First Legal Case
this.process_date_1 = page.locator('#id_LegalSituation-process_date_1'); 
this.investigation_type_1 = page.locator('#id_LegalSituation-investigation_type_1');
this.cause_1 = page.locator('#id_LegalSituation-cause_1'); 
this.authority_1 = page.locator('#id_LegalSituation-autority_1'); 
this.process_state_1 = page.locator('#id_LegalSituation-process_state_1'); 
this.responsible_1 = page.locator('#id_LegalSituation-responsible_1'); 

// Second Legal Case
this.process_date_2 = page.locator('#id_LegalSituation-process_date_2'); 
this.investigation_type_2 = page.locator('#id_LegalSituation-investigation_type_2'); 
this.cause_2 = page.locator('#id_LegalSituation-cause_2'); 
this.authority_2 = page.locator('#id_LegalSituation-autority_2'); 
this.process_state_2 = page.locator('#id_LegalSituation-process_state_2'); 
this.responsible_2 = page.locator('#id_LegalSituation-responsible_2'); 

}


async fillForm() {
  await this.legal_situation_tab.click();

  // First Legal Case
  await this.process_date_1.fill('2019-05-22');
  await this.investigation_type_1.fill('Legal');
  await this.cause_1.fill('Investigation Cause 1');
  await this.authority_1.fill('Comptrollers Office');
  await this.process_state_1.fill('In progress');
  await this.responsible_1.selectOption('No');

  // Second Legal Case
  await this.process_date_2.fill('2014-02-22');
  await this.investigation_type_2.fill('Legal');
  await this.cause_2.fill('Investigation Cause 2');
  await this.authority_2.fill('Inspector Generals Office');
  await this.process_state_2.fill('In progress');
  await this.responsible_2.selectOption('Yes');
}

async fillFormWithErrors() {
  await this.legal_situation_tab.click();

  // First Legal Case
  await this.investigation_type_1.fill('Legal#$%$&');
  await this.cause_1.fill('Investigation Cause 1"$#%&$');
  await this.authority_1.fill('Comptrollers Office"##$%#$#');
  await this.process_state_1.fill('In progress"#$%$');

  // Second Legal Case

  await this.investigation_type_2.fill('Lega#"$#%l');
  await this.cause_2.fill('Investigation Cause 2"#$#%$&');
  await this.authority_2.fill('Inspector Generals Offic"#$%e');
  await this.process_state_2.fill('In progress"#$%&');
}
      getErrorMessageForField(fieldId: string): Locator {
    return this.page.locator(`#${fieldId}_error strong`);
  }

}

