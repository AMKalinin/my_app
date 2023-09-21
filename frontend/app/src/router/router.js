import ProjectsTab from "@/views/ProjectsTab";
import TasksTab from "@/views/TasksTab";
import ViewTab from "@/views/ViewTab";

import {createRouter, createWebHistory} from "vue-router"

const routes = [
    {
        path: '/projects',
        component: ProjectsTab
    },
    {
        path: '/',
        component: ProjectsTab
    },
    {
        path: '/tasks',
        component: TasksTab
    },
    {
        path: '/view',
        component: ViewTab
    }
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router