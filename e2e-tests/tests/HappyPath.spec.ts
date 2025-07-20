import { test, expect } from '@playwright/test';
import { PersonalDataPage } from '../pages/PersonalData.page';
import { FamilyDataPage } from '../pages/FamilyData.page';
import { AcademicInformationPage } from '../pages/AcademicInformation.page';
import { AssetsIncomePage } from '../pages/AssetsIncome.page';
import { LegalSituationPage } from '../pages/LegalSituation.page';


test('Happy Path Form Test', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/');

  //Personal Data
  const personalData = new PersonalDataPage(page);
  await personalData.FillForm();
  const personalDataAddress = await personalData.obtainPersonaDataBuiltAddress();
  expect(personalDataAddress).toBe('Street 69 C BIS A EAST # 69 H WEST 22, Second Floor');
 


//DATOS FAMILIARES
  const FamilyData = new FamilyDataPage(page);
  await FamilyData.FillForm();
  const spouseAddress = await FamilyData.obtainSpousesBuiltAddress();
  const fatherAddress = await FamilyData.obtainFathersBuiltAddress();
  const motherAddress = await FamilyData.obtainMothersBuiltAddress();


const siblingAddress = await FamilyData.getSiblingsAddress(0);
const siblingAddress1 = await FamilyData.getSiblingsAddress(1);



  expect(spouseAddress).toBe('Street 167 A NORTH # 56 B WEST 73, Torre 4 apto 4');
  expect(fatherAddress).toBe('Highway 50 H BIS F SOUTH # 89 J WEST 789, Bosa');
  expect(motherAddress).toBe('Avenue Street 230 O Z NORTH # 566 P EAST 200, third floor');
  expect(siblingAddress).toBe('Alley 50 H BIS F NORTH # 89 P EAST 79, Bosa');
  expect(siblingAddress1).toBe('Circle 50 H BIS F SOUTH # 89 J WEST 789, Bosa');


  
//INFORMACIÓN ACADÉMICA
  const AcademicInformation = new AcademicInformationPage(page);
  await AcademicInformation.FillForm();



//BIENES Y RENTAS
  const AssetsIncome =new AssetsIncomePage(page);
  await AssetsIncome.FillForm();
  const TotalIncomeSum = await AssetsIncome.ObtainTotalIncome();
  expect(TotalIncomeSum).toBe('$989.663.025');

//SITUACIÓN JURÍDICA
  const LegalSituation =new LegalSituationPage(page);
  await LegalSituation.fillForm();

await page.click('button[type="submit"]');
await page.waitForURL('http://127.0.0.1:8000/success/');
expect(page.url()).toBe('http://127.0.0.1:8000/success/');

});
