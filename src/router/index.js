import { createWebHistory, createRouter } from "vue-router";
import Dashboard from "../features/dashboard/views/Dashboard.vue";
import Meeting from "../features/meeting/views/Meeting.vue";

const routes = [
    { path: '/', component: Meeting },
    { path: '/dashboard', component: Dashboard },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;