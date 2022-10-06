import { createRouter, createWebHistory } from 'vue-router'
import DashBoard from '../views/DashBoard.vue'
import CreateAccount from '../views/CreateAccount.vue'
import PouleView from '../views/PouleView.vue'
import InfoPouleView from '../views/pouleInfoView.vue'

const routes = [{
        path: '/dashboard',
        name: 'dashboard',
        component: DashBoard
    },
    {
        path: '/poules',
        name: 'poules',
        component: PouleView
    },
    {
        path: '/infopoule/:id',
        name: 'infopoule',
        component: InfoPouleView
    },
    {
        path: '/create-account',
        name: 'createAccount',
        component: CreateAccount
    },
    {
        path: '/',
        name: 'login',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/LoginView.vue')
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router