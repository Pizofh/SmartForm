import { Page, Locator } from '@playwright/test';

export class AssetsIncomePage {
  readonly page: Page;
  readonly tab: Locator;
  readonly AssetsIncome_tab : Locator; 

//Total income last fiscal year
  readonly salary_and_other_income:Locator
  readonly layoff_and_interests :Locator;
  readonly representation_expenses:Locator;
  readonly leases:Locator;
  readonly fee:Locator;
  readonly other_income:Locator;
  readonly total_income : Locator;

//Bank accounts in Colombia and abroad

  readonly financial_entity_1 : Locator; 
  readonly account_type_1:Locator
  readonly account_number_1 :Locator;
  readonly financial_entity_2 : Locator; 
  readonly account_type_2:Locator
  readonly account_number_2 :Locator;


//Assets
  readonly good_type_1 : Locator;
  readonly good_location_1 :Locator;
  readonly good_id_1 :Locator;
  readonly good_appraisal_1 :Locator;
  
  readonly good_type_2 : Locator;
  readonly good_location_2 :Locator;
  readonly good_id_2 :Locator;
  readonly good_appraisal_2 :Locator;


//Current debts
  readonly obligation_entity_person_1 : Locator;
  readonly obligation_concept_1 : Locator;
  readonly value_1 : Locator;

  readonly obligation_entity_person_2 : Locator;
  readonly obligation_concept_2 : Locator;
  readonly value_2 : Locator;



//Participation in organizations, NGOs, societies

  readonly entity_or_institution_1 :Locator;
  readonly kind_of_member_1 : Locator;

  readonly entity_or_institution_2 :Locator;
  readonly kind_of_member_2 : Locator;



//Private economic activity
    
  readonly company_1 : Locator; 
  readonly kind_of_member_AEP_1: Locator;

  readonly company_2 : Locator;
  readonly kind_of_member_AEP_2: Locator;





constructor(page: Page) {
    this.page = page;
    this.tab = page.locator('text=Bienes Rentas');

//Total income last fiscal year
this.AssetsIncome_tab = page.locator('#formTabs > li:nth-child(4) > button');
this.salary_and_other_income = page.locator('#id_AssetsIncomeAEP-salary_and_other_income');
this.layoff_and_interests = page.locator('#id_AssetsIncomeAEP-layoff_and_interests');
this.representation_expenses = page.locator('#id_AssetsIncomeAEP-representation_expenses');
this.leases = page.locator('#id_AssetsIncomeAEP-leases');
this.fee = page.locator('#id_AssetsIncomeAEP-fee');
this.other_income = page.locator('#id_AssetsIncomeAEP-other_income');
this.total_income = page.locator('#id_AssetsIncomeAEPForm-total_income');


//Bank accounts in Colombia and abroad
this.financial_entity_1 = page.locator('#id_AssetsIncomeAEP-financial_entity_1');
this.account_type_1 = page.locator('#id_AssetsIncomeAEP-account_type_1');
this.account_number_1 = page.locator('#id_AssetsIncomeAEP-account_number_1');

this.financial_entity_2 = page.locator('#id_AssetsIncomeAEP-financial_entity_2');
this.account_type_2 = page.locator('#id_AssetsIncomeAEP-account_type_2');
this.account_number_2 = page.locator('#id_AssetsIncomeAEP-account_number_2');




//Assets
this.good_type_1 = page.locator('#id_AssetsIncomeAEP-good_type_1');
this.good_location_1 = page.locator('#id_AssetsIncomeAEP-good_location_1');
this.good_id_1 = page.locator('#id_AssetsIncomeAEP-good_id_1');
this.good_appraisal_1 = page.locator('#id_AssetsIncomeAEP-good_appraisal_1');

this.good_type_2 = page.locator('#id_AssetsIncomeAEP-good_type_2');
this.good_location_2 = page.locator('#id_AssetsIncomeAEP-good_location_2');
this.good_id_2 = page.locator('#id_AssetsIncomeAEP-good_id_2');
this.good_appraisal_2 = page.locator('#id_AssetsIncomeAEP-good_appraisal_2');


//Current debts
this.obligation_entity_person_1 = page.locator('#id_AssetsIncomeAEP-obligation_entity_person_1');
this.obligation_concept_1 = page.locator('#id_AssetsIncomeAEP-obligation_concept_1');
this.value_1 = page.locator('#id_AssetsIncomeAEP-value_1');

this.obligation_entity_person_2 = page.locator('#id_AssetsIncomeAEP-obligation_entity_person_2');
this.obligation_concept_2 = page.locator('#id_AssetsIncomeAEP-obligation_concept_2');
this.value_2 = page.locator('#id_AssetsIncomeAEP-value_2');



//Participation in organizations, NGOs, societies

this.entity_or_institution_1 = page.locator('#id_AssetsIncomeAEP-entity_or_institution_1');
this.kind_of_member_1 = page.locator('#id_AssetsIncomeAEP-kind_of_member_1');

this.entity_or_institution_2 = page.locator('#id_AssetsIncomeAEP-entity_or_institution_2');
this.kind_of_member_2 = page.locator('#id_AssetsIncomeAEP-kind_of_member_2');




  //Private economic activity
    
this.company_1 = page.locator('#id_AssetsIncomeAEP-company_1');
this.kind_of_member_AEP_1 = page.locator('#id_AssetsIncomeAEP-kind_of_member_AEP_1');

this.company_2 = page.locator('#id_AssetsIncomeAEP-company_2');
this.kind_of_member_AEP_2 = page.locator('#id_AssetsIncomeAEP-kind_of_member_AEP_2');



  }


  async FillForm() {

    await this.AssetsIncome_tab.click();

  //Total income last fiscal year
    await this.salary_and_other_income.fill('123456');
    await this.layoff_and_interests.fill('987654321');
    await this.representation_expenses.fill('741258');
    await this.leases.fill('654987');
    await this.fee.fill('365214');
    await this.other_income.fill('123789');
    await this.total_income 

//Bank accounts in Colombia and abroad

  await this.financial_entity_1.fill('Bank1');
  await this.account_type_1.fill('Savings');
  await this.account_number_1.fill('123456789123457');

  await this.financial_entity_2.fill('Bank 2');
  await this.account_type_2.fill('Stocks');
  await this.account_number_2.fill('987654321963852');


//Assets

  await this.good_type_1.fill('Car');
  await this.good_location_1.fill('Tunja');
  await this.good_id_1.fill('Id3nt1f1c4tion');
  await this.good_appraisal_1.fill('123456789');

  await this.good_type_2.fill('house');
  await this.good_location_2.fill('Yopal');
  await this.good_id_2.fill('123456789'); 
  await this.good_appraisal_2.fill('74125368');



//Current debts
  await this.obligation_entity_person_1.fill('Obligation 1');
  await this.obligation_concept_1.fill('The reason for this');
  await this.value_1.fill('111111');

  await this.obligation_entity_person_2.fill('Obligation 2');
  await this.obligation_concept_2.fill('Reason number two');
  await this.value_2.fill('222222');


//Participation in organizations, NGOs, societies

  await this.entity_or_institution_1.fill('Organization');
  await this.kind_of_member_1.fill('Member 1');

  await this.entity_or_institution_2.fill('Corporation');
  await this.kind_of_member_2.fill('Manager');


  //Private economic activity
    
  await this.company_1.fill('Company 1');
  await this.kind_of_member_AEP_1.fill('President'); 

  await this.company_2.fill('Company 2');
  await this.kind_of_member_AEP_2.fill('Theone'); 

  } 

  async ObtainTotalIncome(): Promise<string> {
  const totalsum = await this.total_income.inputValue();
  return totalsum.trim();
}



async FillFormWithErrors() {

    await this.AssetsIncome_tab.click();

  //Total income last fiscal year
    await this.salary_and_other_income.fill('999999999999999999999999999999999999999999999999999999999999999');
    await this.layoff_and_interests.fill('999999999999999999999999999999999999999999999999999999999999999');
    await this.representation_expenses.fill('999999999999999999999999999999999999999999999999999999999999999');
    await this.leases.fill('999999999999999999999999999999999999999999999999999999999999999');
    await this.fee.fill('999999999999999999999999999999999999999999999999999999999999999');
    await this.other_income.fill('999999999999999999999999999999999999999999999999999999999999999');

//Bank accounts in Colombia and abroad

  await this.financial_entity_1.fill('ADSFE"##$%&Y%');
  await this.account_type_1.fill('ADSFE"##$%&Y%');
  await this.account_number_1.fill('999999999999999999999999999999999999999999999999999999999999999');

  await this.financial_entity_2.fill('ADSFE"##$%&Y%');
  await this.account_type_2.fill('ADSFE"##$%&Y%');
  await this.account_number_2.fill('999999999999999999999999999999999999999999999999999999999999999');


//Assets

  await this.good_type_1.fill('CarADSFE"##$%&Y%');
  await this.good_location_1.fill('TunjaADSFE"##$%&Y%');
  await this.good_id_1.fill('Id3nt1f1c4tionADSFE"##$%&Y%');
  await this.good_appraisal_1.fill('999999999999999999999999999999999999999999999999999999999999999');

  await this.good_type_2.fill('houseADSFE"##$%&Y%');
  await this.good_location_2.fill('YopalADSFE"##$%&Y%');
  await this.good_id_2.fill('123456789ADSFE"##$%&Y%'); 
  await this.good_appraisal_2.fill('999999999999999999999999999999999999999999999999999999999999999');



//Current debts
  await this.obligation_entity_person_1.fill('Obligation ADSFE"##$%&Y%1');
  await this.obligation_concept_1.fill('The reason for thisADSFE"##$%&Y%');
  await this.value_1.fill('999999999999999999999999999999999999999999999999999999999999999');

  await this.obligation_entity_person_2.fill('ObligationADSFE"##$%&Y% 2');
  await this.obligation_concept_2.fill('Reason number ADSFE"##$%&Y%two');
  await this.value_2.fill('999999999999999999999999999999999999999999999999999999999999999');


//Participation in organizations, NGOs, societies

  await this.entity_or_institution_1.fill('OrgADSFE"##$%&Y%anization');
  await this.kind_of_member_1.fill('Member 1ADSFE"##$%&Y%');

  await this.entity_or_institution_2.fill('CorporationADSFE"##$%&Y%');
  await this.kind_of_member_2.fill('ManagerADSFE"##$%&Y%');


  //Private economic activity
    
  await this.company_1.fill('Company 1ADSFE"##$%&Y%');
  await this.kind_of_member_AEP_1.fill('PresidentADSFE"##$%&Y%'); 

  await this.company_2.fill('Company 2ADSFE"##$%&Y%');
  await this.kind_of_member_AEP_2.fill('TheoneADSFE"##$%&Y%'); 


  
  }
  
      getErrorMessageForField(fieldId: string): Locator {
    return this.page.locator(`#${fieldId}_error strong`);
  }
}