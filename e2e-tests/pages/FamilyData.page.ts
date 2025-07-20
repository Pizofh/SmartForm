import { Page, Locator } from '@playwright/test';

export class FamilyDataPage {
  readonly page: Page;
  readonly tab: Locator;

  //Spouse Data
  readonly FamilyDataTab : Locator;
  readonly spouse_name : Locator;
  readonly spouse_id : Locator;
  readonly spouse_profession : Locator;
  readonly spouse_phone : Locator;
  readonly spouse_street_type : Locator;
  readonly spouse_principal_number : Locator;
  readonly spouse_principal_letter: Locator;
  readonly spouse_bis: Locator;
  readonly spouse_bis_letter : Locator;
  readonly spouse_quadrant: Locator;
  readonly spouse_second_number : Locator;
  readonly spouse_second_letter: Locator;
  readonly spouse_second_quadrant : Locator;
  readonly spouse_nmbr : Locator;
  readonly spouse_complement : Locator;
  readonly spouse_built_address : Locator;

  //Father's Data
  readonly father_name : Locator;
  readonly father_lives: Locator;
  readonly father_id: Locator; 
  readonly father_phone : Locator;
  readonly father_profession : Locator;
  readonly father_street_type: Locator;
  readonly father_principal_number : Locator;
  readonly father_principal_letter: Locator;
  readonly father_bis: Locator;
  readonly father_bis_letter : Locator;
  readonly father_quadrant : Locator;
  readonly father_second_number: Locator;
  readonly father_second_letter : Locator;
  readonly father_second_quadrant: Locator;
  readonly father_nmbr : Locator;
  readonly father_complement: Locator;
  readonly father_built_address : Locator;

  //Mother's Data
  readonly mother_name: Locator;
  readonly mother_lives : Locator;
  readonly mother_id : Locator;
  readonly mother_phone: Locator;
  readonly mother_profession: Locator;
  readonly mother_street_type : Locator;
  readonly mother_principal_number : Locator;
  readonly mother_principal_letter: Locator;
  readonly mother_bis: Locator;
  readonly mother_bis_letter : Locator;
  readonly mother_quadrant: Locator;
  readonly mother_second_number : Locator;
  readonly mother_second_letter: Locator;
  readonly mother_second_quadrant: Locator;
  readonly mother_nmbr : Locator;
  readonly mother_complement: Locator;
  readonly mother_built_address : Locator;

  //Children's Data
  readonly name: Locator;
  readonly age : Locator;
  readonly child_id : Locator;
  readonly name_1: Locator;
  readonly age_1 : Locator;
  readonly child_id_1 : Locator;
  readonly add_child : Locator;
  readonly delete_child : Locator;

  //Siblings' Data
  readonly sibling_lastname: Locator;
  readonly sibling_second_lastname: Locator;
  readonly sibling_first_name: Locator;
  readonly sibling_second_name: Locator;
  readonly sibling_id : Locator;
  readonly sibling_occupation :Locator;
  readonly sibling_phone: Locator;
  readonly sibling_street_type: Locator;
  readonly sibling_principal_number: Locator;
  readonly sibling_principal_letter: Locator;
  readonly sibling_bis: Locator;
  readonly sibling_bis_letter: Locator;
  readonly sibling_quadrant: Locator;
  readonly sibling_second_number: Locator;
  readonly sibling_second_letter: Locator;
  readonly sibling_second_quadrant: Locator;
  readonly sibling_nmbr: Locator;
  readonly sibling_complement: Locator;
  readonly sibling_built_address: Locator;

  readonly add_sibling  :Locator;
  readonly sibling_lastname_1: Locator;
  readonly sibling_second_lastname_1: Locator;
  readonly sibling_first_name_1: Locator;
  readonly sibling_second_name_1: Locator;
  readonly sibling_id_1 : Locator;
  readonly sibling_occupation_1 :Locator;
  readonly sibling_phone_1: Locator;
  readonly sibling_street_type_1: Locator;
  readonly sibling_principal_number_1: Locator;
  readonly sibling_principal_letter_1: Locator;
  readonly sibling_bis_1: Locator;
  readonly sibling_bis_letter_1: Locator;
  readonly sibling_quadrant_1: Locator;
  readonly sibling_second_number_1: Locator;
  readonly sibling_second_letter_1: Locator;
  readonly sibling_second_quadrant_1: Locator;
  readonly sibling_nmbr_1: Locator;
  readonly sibling_complement_1: Locator;
  readonly sibling_built_address_1: Locator;


    constructor(page: Page) {
      this.page = page;
      this.tab = page.locator('text=Family Data');
      this.FamilyDataTab=page.locator('#tab-family-data');

  ////Spouse Data

  this.spouse_name = page.locator('#id_FamilyData-spouse_name')
  this.spouse_id = page.locator('#id_FamilyData-spouse_id')
  this.spouse_profession = page.locator('#id_FamilyData-spouse_profession')
  this.spouse_phone = page.locator('#id_FamilyData-spouse_phone')
  this.spouse_street_type = page.locator('#id_FamilyData-spouse_street_type')
  this.spouse_principal_number = page.locator('#id_FamilyData-spouse_principal_number')
  this.spouse_principal_letter = page.locator('#id_FamilyData-spouse_principal_letter')
  this.spouse_bis = page.locator('#id_FamilyData-spouse_bis')
  this.spouse_bis_letter = page.locator('#id_FamilyData-spouse_bis_letter')
  this.spouse_quadrant = page.locator('#id_FamilyData-spouse_quadrant')
  this.spouse_second_number = page.locator('#id_FamilyData-spouse_second_number')
  this.spouse_second_letter = page.locator('#id_FamilyData-spouse_second_letter')
  this.spouse_second_quadrant = page.locator('#id_FamilyData-spouse_second_quadrant')
  this.spouse_nmbr = page.locator('#id_FamilyData-spouse_nmbr')
  this.spouse_complement = page.locator('#id_FamilyData-spouse_complement')
  this.spouse_built_address = page.locator('#spouse_preview_address')

  //Father's Data
  this.father_name = page.locator('#id_FamilyData-father_name')
  this.father_lives = page.locator('#id_FamilyData-father_lives')
  this.father_id = page.locator('#id_FamilyData-father_id')
  this.father_phone = page.locator('#id_FamilyData-father_phone')
  this.father_profession = page.locator('#id_FamilyData-father_profession')
  this.father_street_type = page.locator('#id_FamilyData-father_street_type')
  this.father_principal_number = page.locator('#id_FamilyData-father_principal_number')
  this.father_principal_letter = page.locator('#id_FamilyData-father_principal_letter')
  this.father_bis = page.locator('#id_FamilyData-father_bis')
  this.father_bis_letter = page.locator('#id_FamilyData-father_bis_letter')
  this.father_quadrant = page.locator('#id_FamilyData-father_quadrant')
  this.father_second_number = page.locator('#id_FamilyData-father_second_number')
  this.father_second_letter = page.locator('#id_FamilyData-father_second_letter')
  this.father_second_quadrant = page.locator('#id_FamilyData-father_second_quadrant')
  this.father_nmbr = page.locator('#id_FamilyData-father_nmbr')
  this.father_complement = page.locator('#id_FamilyData-father_complement')
  this.father_built_address = page.locator('#father_preview_address')  

  //Mother's Data
  this.mother_name = page.locator('#id_FamilyData-mother_name')
  this.mother_lives = page.locator('#id_FamilyData-mother_lives')
  this.mother_id = page.locator('#id_FamilyData-mother_id')
  this.mother_phone = page.locator('#id_FamilyData-mother_phone')
  this.mother_profession = page.locator('#id_FamilyData-mother_profession')
  this.mother_street_type = page.locator('#id_FamilyData-mother_street_type')
  this.mother_principal_number = page.locator('#id_FamilyData-mother_principal_number')
  this.mother_principal_letter = page.locator('#id_FamilyData-mother_principal_letter')
  this.mother_bis = page.locator('#id_FamilyData-mother_bis')
  this.mother_bis_letter = page.locator('#id_FamilyData-mother_bis_letter')
  this.mother_quadrant = page.locator('#id_FamilyData-mother_quadrant')
  this.mother_second_number = page.locator('#id_FamilyData-mother_second_number')
  this.mother_second_letter = page.locator('#id_FamilyData-mother_second_letter')
  this.mother_second_quadrant = page.locator('#id_FamilyData-mother_second_quadrant')
  this.mother_nmbr = page.locator('#id_FamilyData-mother_nmbr')
  this.mother_complement = page.locator('#id_FamilyData-mother_complement')
  this.mother_built_address = page.locator('#mother_preview_address')

    //Children data
    this.name = page.locator('#id_Child-0-name');
    this.age = page.locator('#id_Child-0-age');
    this.child_id = page.locator('#id_Child-0-child_id');
    this.add_child = page.locator('#add-Child');
    this.delete_child = page.locator('.delete-Child').nth(2);
    this.name_1 = page.locator('#id_Child-1-name')
    this.age_1 = page.locator('#id_Child-1-age')
    this.child_id_1 =page.locator('#id_Child-1-child_id')

    //Siblings data
  this.sibling_lastname = page.locator('#id_Sibling-0-sibling_lastname');
  this.sibling_second_lastname = page.locator('#id_Sibling-0-sibling_second_lastname');
  this.sibling_first_name = page.locator('#id_Sibling-0-sibling_first_name');
  this.sibling_second_name = page.locator('#id_Sibling-0-sibling_second_name');
  this.sibling_id = page.locator('#id_Sibling-0-sibling_id');
  this.sibling_occupation = page.locator('#id_Sibling-0-sibling_occupation');
  this.sibling_phone = page.locator('#id_Sibling-0-sibling_phone');
  this.add_sibling = page.locator('//*[@id="add-Sibling"]');
  this.sibling_street_type = page.locator('#id_Sibling-0-sibling_street_type');
  this.sibling_principal_number = page.locator('#id_Sibling-0-sibling_principal_number');
  this.sibling_principal_letter = page.locator('#id_Sibling-0-sibling_principal_letter');
  this.sibling_bis = page.locator('#id_Sibling-0-sibling_bis');
  this.sibling_bis_letter = page.locator('#id_Sibling-0-sibling_bis_letter');
  this.sibling_quadrant = page.locator('#id_Sibling-0-sibling_quadrant');
  this.sibling_second_number = page.locator('#id_Sibling-0-sibling_second_number');
  this.sibling_second_letter = page.locator('#id_Sibling-0-sibling_second_letter');
  this.sibling_second_quadrant = page.locator('#id_Sibling-0-sibling_second_quadrant');
  this.sibling_nmbr = page.locator('#id_Sibling-0-sibling_nmbr');
  this.sibling_complement = page.locator('#id_Sibling-0-sibling_complement');
  this.sibling_built_address = page.locator('//*[@id="formset-Sibling"]/div[1]/div/div[5]');

  this.sibling_lastname_1 = page.locator('#id_Sibling-1-sibling_lastname');
  this.sibling_second_lastname_1 = page.locator('#id_Sibling-1-sibling_second_lastname');
  this.sibling_first_name_1 = page.locator('#id_Sibling-1-sibling_first_name');
  this.sibling_second_name_1 = page.locator('#id_Sibling-1-sibling_second_name');
  this.sibling_id_1 = page.locator('#id_Sibling-1-sibling_id');
  this.sibling_occupation_1 = page.locator('#id_Sibling-1-sibling_occupation');
  this.sibling_phone_1 = page.locator('#id_Sibling-1-sibling_phone');
  this.sibling_street_type_1 = page.locator('#id_Sibling-1-sibling_street_type');
  this.sibling_principal_number_1 = page.locator('#id_Sibling-1-sibling_principal_number');
  this.sibling_principal_letter_1 = page.locator('#id_Sibling-1-sibling_principal_letter');
  this.sibling_bis_1 = page.locator('#id_Sibling-1-sibling_bis');
  this.sibling_bis_letter_1 = page.locator('#id_Sibling-1-sibling_bis_letter');
  this.sibling_quadrant_1 = page.locator('#id_Sibling-1-sibling_quadrant');
  this.sibling_second_number_1 = page.locator('#id_Sibling-1-sibling_second_number');
  this.sibling_second_letter_1 = page.locator('#id_Sibling-1-sibling_second_letter');
  this.sibling_second_quadrant_1 = page.locator('#id_Sibling-1-sibling_second_quadrant');
  this.sibling_nmbr_1 = page.locator('#id_Sibling-1-sibling_nmbr');
  this.sibling_complement_1 = page.locator('#id_Sibling-1-sibling_complement');
  this.sibling_built_address_1 = page.locator('//*[@id="formset-Sibling"]/div[2]/div/div[5]');


    }


    async FillForm() {

//Spouse Data
    await this.FamilyDataTab.click();
    await this.spouse_name.fill('María Rodriguez Tribiño');
    await this.spouse_id.fill('1001346476');
    await this.spouse_profession.fill('Veterinaria');
    await this.spouse_phone.fill('3153111284');
    await this.spouse_street_type.selectOption('Street');
    await this.spouse_principal_number.fill('167');
    await this.spouse_principal_letter.selectOption('A');
    await this.spouse_bis.uncheck();
    await this.spouse_bis_letter
    await this.spouse_quadrant.selectOption('NORTH');
    await this.spouse_second_number.fill('56');
    await this.spouse_second_letter.selectOption('B');
    await this.spouse_second_quadrant.selectOption('WEST');
    await this.spouse_nmbr.fill('73');
    await this.spouse_complement.fill('Torre 4 apto 4');
    await this.spouse_built_address

  //Father's data
    await this.father_name.fill('Johny Garnica Jimenez');
    await this.father_lives.selectOption('Yes');
    await this.father_id.fill('7111397');
    await this.father_phone.fill('3017355009');
    await this.father_profession.fill('Independiente');
    await this.father_street_type.selectOption('Highway');
    await this.father_principal_number.fill('50');
    await this.father_principal_letter.selectOption('H');
    await this.father_bis.check();
    await this.father_bis_letter.selectOption('F');
    await this.father_quadrant.selectOption('SOUTH');
    await this.father_second_number.fill('89');
    await this.father_second_letter.selectOption('J');
    await this.father_second_quadrant.selectOption('WEST');
    await this.father_nmbr.fill('789');
    await this.father_complement.fill('Bosa');
    await this.father_built_address

  //Mother's Data
    await this.mother_name.fill('Milena Sandoval Villamil');
    await this.mother_lives.selectOption('Yes');
    await this.mother_id.fill('40046564');
    await this.mother_phone.fill('3111190645');
    await this.mother_profession.fill('Abogada');
    await this.mother_street_type.selectOption('Avenue Street');
    await this.mother_principal_number.fill('230');
    await this.mother_principal_letter.selectOption('O');
    await this.mother_bis.uncheck();
    await this.mother_bis_letter.selectOption('Z'); 
    await this.mother_quadrant.selectOption('NORTH');
    await this.mother_second_number.fill('566');
    await this.mother_second_letter.selectOption('P');
    await this.mother_second_quadrant.selectOption('EAST');
    await this.mother_nmbr.fill('200');
    await this.mother_complement.fill('third floor');
    await this.mother_built_address

  //Children Data 
    await this.name.fill('Rocko');
    await this.age.fill('9');
    await this.child_id.fill('1351386');
    await this.add_child.click();
    await this.add_child.click();
    await this.name_1.fill('Chispun');
    await this.age_1.fill('2');
    await this.child_id_1.fill('19128731');
    await this.delete_child.click();

  //Siblings Data

    await this.sibling_lastname.fill('Garnica');
    await this.sibling_second_lastname.fill('Sandoval');
    await this.sibling_first_name.fill('Melany');
    await this.sibling_second_name
    await this.sibling_id.fill('53513525');
    await this.sibling_occupation.fill('Student');
    await this.sibling_phone.fill('3139946548');
    await this.sibling_street_type.selectOption('Alley');
    await this.sibling_principal_number.fill('50');
    await this.sibling_principal_letter.selectOption('H');
    await this.sibling_bis.check();
    await this.sibling_bis_letter.selectOption('F');
    await this.sibling_quadrant.selectOption('NORTH');
    await this.sibling_second_number.fill('89');
    await this.sibling_second_letter.selectOption('P');
    await this.sibling_second_quadrant.selectOption('EAST');
    await this.sibling_nmbr.fill('79');
    await this.sibling_complement.fill('Bosa');

    await this.add_sibling.click();


    await this.sibling_lastname_1.fill('Garnicaasdasd');
    await this.sibling_second_lastname_1.fill('Sandovaldsadas');
    await this.sibling_first_name_1.fill('Melanyasdasda');
    await this.sibling_second_name_1
    await this.sibling_id_1.fill('535131561');
    await this.sibling_occupation_1.fill('Estudianteeee');
    await this.sibling_phone_1.fill('3136566515');
    await this.sibling_street_type_1.selectOption('Circle');
    await this.sibling_principal_number_1.fill('50');
    await this.sibling_principal_letter_1.selectOption('H');
    await this.sibling_bis_1.check();
    await this.sibling_bis_letter_1.selectOption('F');
    await this.sibling_quadrant_1.selectOption('SOUTH');
    await this.sibling_second_number_1.fill('89');
    await this.sibling_second_letter_1.selectOption('J');
    await this.sibling_second_quadrant_1.selectOption('WEST');
    await this.sibling_nmbr_1.fill('789');
    await this.sibling_complement_1.fill('Bosa');

    } 


    async obtainSpousesBuiltAddress(): Promise<string> {
    const SpousesBuiltAddress = await this.spouse_built_address.textContent();
    return SpousesBuiltAddress?.trim() ?? '';
  }
    async obtainFathersBuiltAddress(): Promise<string> {
    const FathersBuiltAddress = await this.father_built_address.textContent();
    return FathersBuiltAddress?.trim() ?? '';
  }
    async obtainMothersBuiltAddress(): Promise<string> {
    const MothersBuiltAddress = await this.mother_built_address.textContent();
    return MothersBuiltAddress?.trim() ?? '';
  }


  async getSiblingsAddress(index: number): Promise<string> {
    return await this.page
      .locator('input[type="hidden"][name$="sibling_built_address"]') // busca todos los inputs ocultos con ese nombre al final
      .nth(index) // selecciona el índice deseado
      .inputValue(); // obtiene el value del input
  }


    async obtainSiblingsBuiltAddress(): Promise<string> {
    const SiblingsBuiltAddress = await this.sibling_built_address.textContent();
    return SiblingsBuiltAddress?.trim() ?? '';
  }

    async obtainSiblingsBuiltAddress1(): Promise<string> {
    const SiblingsBuiltAddress1 = await this.sibling_built_address_1.textContent();
    return SiblingsBuiltAddress1?.trim() ?? '';
  }


    getErrorMessageForField(fieldId: string): Locator {
    return this.page.locator(`#${fieldId}_error strong`);
  }


    async FillFormWithErrors() {

//CONYUGUE

    await this.FamilyDataTab.click();
    await this.spouse_name.fill('WFER#""#$');
    await this.spouse_id.fill('1');
    await this.spouse_profession.fill('FGRT%&/');
    await this.spouse_phone.fill('2');

//DATOS PADRE
    await this.father_name.fill('FRGTRHY&%$#');
    await this.father_id.fill('1');
    await this.father_phone.fill('1');
    await this.father_profession.fill('#"$RETGRER#$"');


  //DATOS MADRE
    await this.mother_name.fill('RGTRHUYJ&/%');
    await this.mother_id.fill('1999999999999999999999999999999999999999');
    await this.mother_phone.fill('1');
    await this.mother_profession.fill('FGRT%$#"QQ#"');


  //DATOS HIJOS
    await this.name.fill('EDWRFGT$%#"$%');
    await this.age.fill('999999999');
    await this.child_id.fill('1');


  //DATOS HERMANOS

    await this.sibling_lastname.fill('&%$RTGGBFF');
    await this.sibling_second_lastname.fill('#"$%T#$RFEGRVF');
    await this.sibling_first_name.fill('#"$%$#ERFVG');
    await this.sibling_second_name.fill('QEDWEFVRGT%#$"$#"#')
    await this.sibling_id.fill('25');
    await this.sibling_occupation.fill('E$#%&/(/UTYGFe');
    await this.sibling_phone.fill('3139946548222222222222');


    }

}
