import { defineConfig } from '@playwright/test';

export default defineConfig({
  timeout:90*1000,
  testDir: './tests',
  projects: [
    {
      name: 'slow-debug',
      use: {
        baseURL: 'http://127.0.0.1:8000',
        headless: false,
        trace: 'on-first-retry',
        // 👇 slowMo va aquí dentro de "use" cuando usas projects
        launchOptions: {
          //slowMo: 100,
        env: {
         IS_E2E_TEST: 'true',
        },
        },
      },
    },
  ],
}
);
