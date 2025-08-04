import { test, expect } from '@playwright/test';
import { PersonalDataPage } from '../pages/PersonalData.page';
import { FamilyDataPage } from '../pages/FamilyData.page';
import { AcademicInformationPage } from '../pages/AcademicInformation.page';
import { AssetsIncomePage} from '../pages/AssetsIncome.page';
import { LegalSituationPage } from '../pages/LegalSituation.page';

test('Forms: displays validation errors when constraints are violated', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/');
  
  const PersonalData = new PersonalDataPage(page);
  await PersonalData.FillFormWithErrors();

  const FamilyData = new FamilyDataPage(page);
  await FamilyData.FillFormWithErrors();

  const AcademicInfo = new AcademicInformationPage(page);
  await AcademicInfo.FillFormWithErrors();

  const AssetsIncome = new AssetsIncomePage(page);
  await AssetsIncome.FillFormWithErrors();

  const LegalSituation = new LegalSituationPage(page);
  await LegalSituation.fillFormWithErrors();

  await page.click('button[type="submit"]');

//PERSONAL DATA

  await expect(PersonalData.getErrorMessageForField('id_PersonalData-first_name'))
  .toHaveText('Only letters and spaces are allowed.');

  await expect(PersonalData.getErrorMessageForField('id_PersonalData-second_name'))
  .toHaveText('Only letters and spaces are allowed.');

  await expect(PersonalData.getErrorMessageForField('id_PersonalData-lastname'))
  .toHaveText('Only letters and spaces are allowed.');

  await expect(PersonalData.getErrorMessageForField('id_PersonalData-second_lastname'))
  .toHaveText('Only letters and spaces are allowed.');

  await expect(PersonalData.getErrorMessageForField('id_PersonalData-document_number'))
  .toHaveText('Ensure this value is greater than or equal to 1000.');

  await expect(PersonalData.getErrorMessageForField('id_PersonalData-expedition_place'))
  .toHaveText('Only letters and spaces are allowed.');

  await expect(PersonalData.getErrorMessageForField('id_PersonalData-passport_number'))
  .toHaveText('Only letters, numbers, and spaces are allowed.');

  await expect(PersonalData.getErrorMessageForField('id_PersonalData-birth_year'))
  .toHaveText('Ensure this value is less than or equal to 2025.');

  await expect(PersonalData.getErrorMessageForField('id_PersonalData-profession'))
  .toHaveText('Only letters and spaces are allowed.');


  await expect(PersonalData.getErrorMessageForField('id_PersonalData-profesional_id'))
  .toHaveText('Only letters, numbers, and spaces are allowed.');

  await expect(PersonalData.getErrorMessageForField('id_PersonalData-body_marks'))
  .toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

  await expect(PersonalData.getErrorMessageForField('id_PersonalData-height'))
  .toHaveText('Ensure this value is greater than or equal to 80.');

  await expect(PersonalData.getErrorMessageForField('id_PersonalData-weight'))
  .toHaveText('Ensure this value is less than or equal to 500.');

  await expect(PersonalData.getErrorMessageForField('id_PersonalData-neighborhood'))
  .toHaveText('Only letters, numbers, and spaces are allowed.');

  await expect(PersonalData.getErrorMessageForField('id_PersonalData-phone_number'))
  .toHaveText('Ensure this value is greater than or equal to 1000.');

  await expect(PersonalData.getErrorMessageForField('id_PersonalData-city'))
  .toHaveText('Only letters and spaces are allowed.');

  await expect(PersonalData.getErrorMessageForField('id_PersonalData-department'))
  .toHaveText('Only letters and spaces are allowed.');

  await expect(PersonalData.getErrorMessageForField('id_PersonalData-personal_email'))
  .toHaveText('Enter a valid email address.');
  
// DATOS FAMILIARES
  
  await FamilyData.FamilyDataTab.click();


  await expect(FamilyData.getErrorMessageForField('id_FamilyData-spouse_name'))
  .toHaveText("Only letters and spaces are allowed.");

await expect(FamilyData.getErrorMessageForField('id_FamilyData-spouse_id'))
  .toHaveText("Ensure this value is greater than or equal to 1000.");

await expect(FamilyData.getErrorMessageForField('id_FamilyData-spouse_profession'))
  .toHaveText("Only letters and spaces are allowed.");

await expect(FamilyData.getErrorMessageForField('id_FamilyData-spouse_phone'))
  .toHaveText("Ensure this value is greater than or equal to 1000.");

      // DATOS PADRE    


await expect(FamilyData.getErrorMessageForField('id_FamilyData-father_name'))
  .toHaveText('Only letters and spaces are allowed.');

await expect(FamilyData.getErrorMessageForField('id_FamilyData-father_id'))
  .toHaveText('Ensure this value is greater than or equal to 100.');

await expect(FamilyData.getErrorMessageForField('id_FamilyData-father_phone'))
  .toHaveText('Ensure this value is greater than or equal to 100.');

await expect(FamilyData.getErrorMessageForField('id_FamilyData-father_profession'))
  .toHaveText('Only letters and spaces are allowed.');



  // DATOS MADRE


await expect(FamilyData.getErrorMessageForField('id_FamilyData-mother_name'))
  .toHaveText('Only letters and spaces are allowed.');

await expect(FamilyData.getErrorMessageForField('id_FamilyData-mother_id'))
  .toHaveText('Ensure this value is less than or equal to 99999999999.');

await expect(FamilyData.getErrorMessageForField('id_FamilyData-mother_phone'))
  .toHaveText('Ensure this value is greater than or equal to 100.');

await expect(FamilyData.getErrorMessageForField('id_FamilyData-mother_profession'))
  .toHaveText('Only letters and spaces are allowed.');


  
// DATOS HIJO


  await expect(FamilyData.getErrorMessageForField('id_Child-0-name'))
  .toHaveText('Only letters and spaces are allowed.');

  await expect(FamilyData.getErrorMessageForField('id_Child-0-age'))
  .toHaveText('Ensure this value is less than or equal to 200.');


    
// DATOS HERMANO


  await expect(FamilyData.getErrorMessageForField('id_Sibling-0-sibling_lastname'))
  .toHaveText('Only letters and spaces are allowed.');

await expect(FamilyData.getErrorMessageForField('id_Sibling-0-sibling_second_lastname'))
  .toHaveText('Only letters and spaces are allowed.');

await expect(FamilyData.getErrorMessageForField('id_Sibling-0-sibling_first_name'))
  .toHaveText('Only letters and spaces are allowed.');

await expect(FamilyData.getErrorMessageForField('id_Sibling-0-sibling_second_name'))
  .toHaveText('Only letters and spaces are allowed.');

await expect(FamilyData.getErrorMessageForField('id_Sibling-0-sibling_id'))
  .toHaveText('Ensure this value is greater than or equal to 100.');

await expect(FamilyData.getErrorMessageForField('id_Sibling-0-sibling_occupation'))
  .toHaveText('Only letters and spaces are allowed.');

await expect(FamilyData.getErrorMessageForField('id_Sibling-0-sibling_phone'))
  .toHaveText('Ensure this value is less than or equal to 99999999999.');



// ACADEMIC INFORMATION

 await AcademicInfo.academic_information_tab.click();

await expect(AcademicInfo.getErrorMessageForField('id_AcademicInformation-studies_1'))
  .toHaveText('Only letters and spaces are allowed.');

await expect(AcademicInfo.getErrorMessageForField('id_AcademicInformation-studies_1_year'))
  .toHaveText('Ensure this value is greater than or equal to 1900.');

await expect(AcademicInfo.getErrorMessageForField('id_AcademicInformation-studies_title_1'))
  .toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AcademicInfo.getErrorMessageForField('id_AcademicInformation-studies_institution_name_1'))
  .toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AcademicInfo.getErrorMessageForField('id_AcademicInformation-studies_city_1'))
  .toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AcademicInfo.getErrorMessageForField('id_AcademicInformation-studies_2'))
  .toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AcademicInfo.getErrorMessageForField('id_AcademicInformation-studies_2_year'))
  .toHaveText('Ensure this value is less than or equal to 2030.');

await expect(AcademicInfo.getErrorMessageForField('id_AcademicInformation-studies_title_2'))
  .toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AcademicInfo.getErrorMessageForField('id_AcademicInformation-studies_institution_name_2'))
  .toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AcademicInfo.getErrorMessageForField('id_AcademicInformation-studies_city_2'))
  .toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AcademicInfo.getErrorMessageForField('id_AcademicInformation-foreign_language_1'))
  .toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AcademicInfo.getErrorMessageForField('id_AcademicInformation-foreign_language_2'))
  .toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AcademicInfo.getErrorMessageForField('id_AcademicInformation-other_check'))
  .toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');


// ASSETS INCOME 

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-salary_and_other_income'))
.toHaveText('Ensure this value is less than or equal to 999999999999.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-layoff_and_interests'))
.toHaveText('Ensure this value is less than or equal to 999999999999.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-representation_expenses'))
.toHaveText('Ensure this value is less than or equal to 999999999999.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-leases'))
.toHaveText('Ensure this value is less than or equal to 999999999999.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-other_income'))
.toHaveText('Ensure this value is less than or equal to 999999999999.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-financial_entity_1'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-account_type_1'))
.toHaveText('Only letters, numbers, and spaces are allowed.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-account_number_1'))
.toHaveText('Ensure this value is less than or equal to 999999999999999.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-financial_entity_2'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-account_type_2'))
.toHaveText('Only letters, numbers, and spaces are allowed.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-account_number_2'))
.toHaveText('Ensure this value is less than or equal to 999999999999999.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-account_number_2'))
.toHaveText('Ensure this value is less than or equal to 999999999999999.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-good_type_1'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-good_location_1'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-good_id_1'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-good_appraisal_1'))
.toHaveText('Ensure this value is less than or equal to 999999999999999.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-good_type_2'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-good_location_2'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-good_id_2'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-good_appraisal_2'))
.toHaveText('Ensure this value is less than or equal to 999999999999999.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-obligation_entity_person_1'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-obligation_concept_1'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-value_1'))
.toHaveText('Ensure this value is less than or equal to 999999999999999.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-obligation_entity_person_2'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-obligation_concept_2'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-value_2'))
.toHaveText('Ensure this value is less than or equal to 999999999999999.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-entity_or_institution_1'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-kind_of_member_1'))
.toHaveText('Only letters, numbers, and spaces are allowed.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-entity_or_institution_2'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-kind_of_member_2'))
.toHaveText('Only letters, numbers, and spaces are allowed.');

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-company_1'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');  

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-kind_of_member_AEP_1'))
.toHaveText('Only letters, numbers, and spaces are allowed.');  

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-company_2'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');  

await expect(AssetsIncome.getErrorMessageForField('id_AssetsIncomeAEP-kind_of_member_AEP_2'))
.toHaveText('Only letters, numbers, and spaces are allowed.');  

// LEGAL SITUATION

await expect(LegalSituation.getErrorMessageForField('id_LegalSituation-investigation_type_1'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');  

await expect(LegalSituation.getErrorMessageForField('id_LegalSituation-cause_1'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.'); 

await expect(LegalSituation.getErrorMessageForField('id_LegalSituation-autority_1'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.'); 

await expect(LegalSituation.getErrorMessageForField('id_LegalSituation-process_state_1'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.'); 

await expect(LegalSituation.getErrorMessageForField('id_LegalSituation-investigation_type_2'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.');  

await expect(LegalSituation.getErrorMessageForField('id_LegalSituation-cause_2'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.'); 

await expect(LegalSituation.getErrorMessageForField('id_LegalSituation-autority_2'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.'); 

await expect(LegalSituation.getErrorMessageForField('id_LegalSituation-process_state_2'))
.toHaveText('Only letters (including umlauts), numbers, spaces, and basic symbols are allowed.'); 

}); 
