import { test, expect } from '@playwright/test';
import { PersonalDataPage } from '../pages/PersonalData.page';
import { FamilyDataPage } from '../pages/FamilyData.page';
import { AcademicInformationPage } from '../pages/AcademicInformation.page';

test('Forms: displays validation errors when constraints are violated', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/');
  
  const PersonalData = new PersonalDataPage(page);
  await PersonalData.FillFormWithErrors();

  const FamilyData = new FamilyDataPage(page);
  await FamilyData.FillFormWithErrors();

  const AcademicInfo = new AcademicInformationPage(page);
  await AcademicInfo.FillFormWithErrors();

  await page.click('button[type="submit"]');

//RECLUTA

  await expect(PersonalData.getErrorMessageForField('id_recluta-primer_nombre'))
  .toHaveText('Solo se permiten letras y espacios.');

  await expect(PersonalData.getErrorMessageForField('id_recluta-segundo_nombre'))
  .toHaveText('Solo se permiten letras y espacios.');

  await expect(PersonalData.getErrorMessageForField('id_recluta-primer_apellido'))
  .toHaveText('Solo se permiten letras y espacios.');

  await expect(PersonalData.getErrorMessageForField('id_recluta-segundo_apellido'))
  .toHaveText('Solo se permiten letras y espacios.');

  await expect(PersonalData.getErrorMessageForField('id_recluta-numero_documento'))
  .toHaveText('Asegúrese de que este valor es mayor o igual a 1000.');

  await expect(PersonalData.getErrorMessageForField('id_recluta-lugar_expedición'))
  .toHaveText('Solo se permiten letras y espacios.');

  await expect(PersonalData.getErrorMessageForField('id_recluta-pasaporte_numero'))
  .toHaveText('Solo se permiten letras, números y espacios.');

  await expect(PersonalData.getErrorMessageForField('id_recluta-año_nacimiento'))
  .toHaveText('Asegúrese de que este valor es menor o igual a 2025.');

  await expect(PersonalData.getErrorMessageForField('id_recluta-profesion_oficio'))
  .toHaveText('Solo se permiten letras y espacios.');

  await expect(PersonalData.getErrorMessageForField('id_recluta-profesion_oficio'))
  .toHaveText('Solo se permiten letras y espacios.');

  await expect(PersonalData.getErrorMessageForField('id_recluta-tarjeta_profesional'))
  .toHaveText('Solo se permiten letras, números y espacios.');

  await expect(PersonalData.getErrorMessageForField('id_recluta-señales_corporales'))
  .toHaveText('Solo letras (incluyendo diéresis), números, espacios y signos básicos.');

  await expect(PersonalData.getErrorMessageForField('id_recluta-estatura'))
  .toHaveText('Asegúrese de que este valor es mayor o igual a 80.');

  await expect(PersonalData.getErrorMessageForField('id_recluta-peso'))
  .toHaveText('Asegúrese de que este valor es menor o igual a 500.');

  await expect(PersonalData.getErrorMessageForField('id_recluta-barrio'))
  .toHaveText('Solo se permiten letras, números y espacios.');

  await expect(PersonalData.getErrorMessageForField('id_recluta-numero_celular'))
  .toHaveText('Asegúrese de que este valor es mayor o igual a 1000.');

  await expect(PersonalData.getErrorMessageForField('id_recluta-ciudad'))
  .toHaveText('Solo se permiten letras y espacios.');

  await expect(PersonalData.getErrorMessageForField('id_recluta-departamento'))
  .toHaveText('Solo se permiten letras y espacios.');

  await expect(PersonalData.getErrorMessageForField('id_recluta-correo_electronico_personal'))
  .toHaveText('Introduzca una dirección de correo electrónico válida.');
  
// DATOS FAMILIARES
  
  await FamilyData.FamilyDataTab.click();


  await expect(FamilyData.getErrorMessageForField('id_DatosFamiliares-nombre_conyugue'))
  .toHaveText('Solo se permiten letras y espacios.');

  await expect(FamilyData.getErrorMessageForField('id_DatosFamiliares-cedula_conyugue'))
  .toHaveText('Asegúrese de que este valor es mayor o igual a 1000.');

  await expect(FamilyData.getErrorMessageForField('id_DatosFamiliares-profesion_oficio_conyugue'))
  .toHaveText('Solo se permiten letras y espacios.');

    await expect(FamilyData.getErrorMessageForField('id_DatosFamiliares-celular_conyugue'))
  .toHaveText('Asegúrese de que este valor es mayor o igual a 1000.');

      // DATOS PADRE    


  await expect(FamilyData.getErrorMessageForField('id_DatosFamiliares-nombre_padre'))
  .toHaveText('Solo se permiten letras y espacios.');

  await expect(FamilyData.getErrorMessageForField('id_DatosFamiliares-identificación_padre'))
  .toHaveText('Asegúrese de que este valor es mayor o igual a 100.');

  await expect(FamilyData.getErrorMessageForField('id_DatosFamiliares-telefono_padre'))
  .toHaveText('Asegúrese de que este valor es mayor o igual a 100.');

    await expect(FamilyData.getErrorMessageForField('id_DatosFamiliares-oficio_profesion_padre'))
  .toHaveText('Solo se permiten letras y espacios.');


  // DATOS MADRE


  await expect(FamilyData.getErrorMessageForField('id_DatosFamiliares-nombre_madre'))
  .toHaveText('Solo se permiten letras y espacios.');

  await expect(FamilyData.getErrorMessageForField('id_DatosFamiliares-identificación_madre'))
  .toHaveText('Asegúrese de que este valor es menor o igual a 99999999999.');

  await expect(FamilyData.getErrorMessageForField('id_DatosFamiliares-telefono_madre'))
  .toHaveText('Asegúrese de que este valor es mayor o igual a 100.');

    await expect(FamilyData.getErrorMessageForField('id_DatosFamiliares-oficio_profesion_madre'))
  .toHaveText('Solo se permiten letras y espacios.');

  
// DATOS HIJO


  await expect(FamilyData.getErrorMessageForField('id_hijos-0-nombre'))
  .toHaveText('Solo se permiten letras y espacios.');

  await expect(FamilyData.getErrorMessageForField('id_hijos-0-edad'))
  .toHaveText('Asegúrese de que este valor es menor o igual a 200.');


    
// DATOS HERMANO


  await expect(FamilyData.getErrorMessageForField('id_hermanos-0-primer_apellido_hermano'))
  .toHaveText('Solo se permiten letras y espacios.');

  await expect(FamilyData.getErrorMessageForField('id_hermanos-0-segundo_apellido_hermano'))
  .toHaveText('Solo se permiten letras y espacios.');

  await expect(FamilyData.getErrorMessageForField('id_hermanos-0-primer_nombre_hermano'))
  .toHaveText('Solo se permiten letras y espacios.');

  await expect(FamilyData.getErrorMessageForField('id_hermanos-0-segundo_nombre_hermano'))
  .toHaveText('Solo se permiten letras y espacios.');

    await expect(FamilyData.getErrorMessageForField('id_hermanos-0-identificacion_hermano'))
  .toHaveText('Asegúrese de que este valor es mayor o igual a 100.');

  await expect(FamilyData.getErrorMessageForField('id_hermanos-0-ocupacion_hermano'))
  .toHaveText('Solo se permiten letras y espacios.');

  await expect(FamilyData.getErrorMessageForField('id_hermanos-0-celular_hermano'))
  .toHaveText('Asegúrese de que este valor es menor o igual a 99999999999.');


// INFORMACIÓN ACADÉMICA

  await AcademicInfo.academic_information_tab.click();

  await expect(FamilyData.getErrorMessageForField('id_InformacionAcademica-estudios_1'))
  .toHaveText('Solo se permiten letras y espacios.');

  await expect(FamilyData.getErrorMessageForField('id_InformacionAcademica-año_estudios_1'))
  .toHaveText('Asegúrese de que este valor es mayor o igual a 1900.');

  await expect(FamilyData.getErrorMessageForField('id_InformacionAcademica-titulo_estudios_1'))
  .toHaveText('Solo letras (incluyendo diéresis), números, espacios y signos básicos.');

  await expect(FamilyData.getErrorMessageForField('id_InformacionAcademica-nombre_institucion_estudios_1'))
  .toHaveText('Solo letras (incluyendo diéresis), números, espacios y signos básicos.');

    await expect(FamilyData.getErrorMessageForField('id_InformacionAcademica-ciudad_estudios_1'))
  .toHaveText('Solo letras (incluyendo diéresis), números, espacios y signos básicos.');



    await expect(FamilyData.getErrorMessageForField('id_InformacionAcademica-estudios_2'))
  .toHaveText('Solo letras (incluyendo diéresis), números, espacios y signos básicos.');

  await expect(FamilyData.getErrorMessageForField('id_InformacionAcademica-año_estudios_2'))
  .toHaveText('Asegúrese de que este valor es menor o igual a 2030.');

  await expect(FamilyData.getErrorMessageForField('id_InformacionAcademica-titulo_estudios_2'))
  .toHaveText('Solo letras (incluyendo diéresis), números, espacios y signos básicos.');

  await expect(FamilyData.getErrorMessageForField('id_InformacionAcademica-nombre_institucion_estudios_2'))
  .toHaveText('Solo letras (incluyendo diéresis), números, espacios y signos básicos.');

    await expect(FamilyData.getErrorMessageForField('id_InformacionAcademica-ciudad_estudios_2'))
  .toHaveText('Solo letras (incluyendo diéresis), números, espacios y signos básicos.');


    await expect(FamilyData.getErrorMessageForField('id_InformacionAcademica-idioma_extranjero_1'))
  .toHaveText('Solo letras (incluyendo diéresis), números, espacios y signos básicos.');

    await expect(FamilyData.getErrorMessageForField('id_InformacionAcademica-idioma_extranjero_2'))
  .toHaveText('Solo letras (incluyendo diéresis), números, espacios y signos básicos.');




    await expect(FamilyData.getErrorMessageForField('id_InformacionAcademica-otro_check'))
  .toHaveText('Solo letras (incluyendo diéresis), números, espacios y signos básicos.');


}); 
