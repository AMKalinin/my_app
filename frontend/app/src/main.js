import { createApp } from 'vue';
import App from './App';
import PrimeVue from 'primevue/config';
import "primevue/resources/themes/lara-light-indigo/theme.css";

import Button from "primevue/button"
import Menubar from "primevue/menubar"
import 'primeicons/primeicons.css';
import router from './router/router';


const app = createApp(App);

app.use(PrimeVue, { ripple: true  });
app.use(router)

app.component('my-button', Button);
app.component('my-menubar', Menubar)
app.mount('#app')
