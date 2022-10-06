import { createRouter, createWebHistory } from 'vue-router'
import DashBoard from '../views/DashBoard.vue'
import CreateAccount from '../views/CreateAccount.vue'
import PouleView from '../views/PouleView.vue'
import InfoPouleView from '../views/pouleInfoView.vue'
import NotFound from '../views/NotFound.vue'
import GuideView from '../views/GuideView.vue'
import ConditionsView from '../views/ConditionsView.vue'

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
        path: '/infopoule/:pouleId',
        name: 'infopoule',
        component: InfoPouleView,
        props: true
    },
    {
        path: '/create-account',
        name: 'createAccount',
        component: CreateAccount
    },
    {
        path: '/guide',
        name: 'guide',
        component: GuideView
    },
    {
        path: '/conditions',
        name: 'conditions',
        component: ConditionsView
    },
    {
        path: '/',
        name: 'login',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/LoginView.vue')
    },
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router