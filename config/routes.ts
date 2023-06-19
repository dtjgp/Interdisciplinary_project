export default [
  {
    path: '/user',
    layout: false,
    routes: [
      {
        path: '/user/login',
        name: 'login',
        component: './user/Login',
      },
      {
        path: '/user',
        redirect: '/user/login',
      },
      {
        component: './404',
      },
    ],
  },
  {
    path: '/welcome_admin',
    name: 'welcome',
    icon: 'smile',
    component: './Welcome_admin',
    access: 'canAdmin',
  },
   {
     path: '/welcome_user1',
     name: 'welcome',
     icon: 'smile',
     component: './Welcome_user',
     access: 'canUser1',
   },
   {
    path: '/welcome_user2',
    name: 'welcome',
    icon: 'smile',
    component: './Welcome_user',
    access: 'canUser2',
  },
  {
    path: '/welcome_user3',
    name: 'welcome',
    icon: 'smile',
    component: './Welcome_user',
    access: 'canUser3',
  },
  {
    path: '/welcome_user4',
    name: 'welcome',
    icon: 'smile',
    component: './Welcome_user',
    access: 'canUser4',
  },
  {
    path: '/welcome_user5',
    name: 'welcome',
    icon: 'smile',
    component: './Welcome_user',
    access: 'canUser5',
  },

  {
    path: '/admin',
    name: 'Regulator',
    icon: 'crown',
    access: 'canAdmin',
    routes: [
      {
        path: '/admin/admin_before',
        name: 'Before self-modification',
        icon: 'smile',
        component: './admin_before',
      },
      {
        path: '/admin/admin_after',
        name: 'After self-modification',
        icon: 'smile',
        component: './admin_after',
      },

      {
        path: '/admin/user1_history',
        name: 'History',
        icon: 'smile',
        component: './user_history/user1_history',
        access: 'canUser1',
      },
      {
        path: '/admin/user2_history',
        name: 'History',
        icon: 'smile',
        component: './user_history/user2_history',
        access: 'canUser2',
      },
      {
        path: '/admin/user3_history',
        name: 'History',
        icon: 'smile',
        component: './user_history/user3_history',
        access: 'canUser3',
      },
      {
        path: '/admin/user4_history',
        name: 'History',
        icon: 'smile',
        component: './user_history/user4_history',
        access: 'canUser4',
      },
      {
        path: '/admin/user5_history',
        name: 'History',
        icon: 'smile',
        component: './user_history/user5_history',
        access: 'canUser5',
      },    
      
      {
        path: '/admin/user1_prediction',
        name: 'Prediction',
        icon: 'smile',
        component: './user_prediction/user1_prediction',
        access: 'canUser1',
      },
      {
        path: '/admin/user2_prediction',
        name: 'Prediction',
        icon: 'smile',
        component: './user_prediction/user2_prediction',
        access: 'canUser2',
      },
      {
        path: '/admin/user3_prediction',
        name: 'Prediction',
        icon: 'smile',
        component: './user_prediction/user3_prediction',
        access: 'canUser3',
      },
      {
        path: '/admin/user4_prediction',
        name: 'Prediction',
        icon: 'smile',
        component: './user_prediction/user4_prediction',
        access: 'canUser4',
      },
      {
        path: '/admin/user5_prediction',
        name: 'Prediction',
        icon: 'smile',
        component: './user_prediction/user5_prediction',
        access: 'canUser5',
      },
      {
        component: './404',
      },
    ],
  },

  {
    path: '/admin',
    name: 'Iren',
    icon: 'crown',
    access: 'canUser1',
    routes: [
      {
        path: '/admin/user1_history',
        name: 'History',
        icon: 'smile',
        component: './user_history/user1_history',
      },
      {
        path: '/admin/user1_prediction',
        name: 'Prediction',
        icon: 'smile',
        component: './user_prediction/user1_prediction',
      },
      {
        component: './404',
      },
    ],
  },

  {
    path: '/admin',
    name: 'Alperia',
    icon: 'crown',
    access: 'canUser2',
    routes: [
      {
        path: '/admin/user2_history',
        name: 'History',
        icon: 'smile',
        component: './user_history/user2_history',
      },
      {
        path: '/admin/user2_prediction',
        name: 'Prediction',
        icon: 'smile',
        component: './user_prediction/user2_prediction',
      },
      {
        component: './404',
      },
    ],
  },
  {
    path: '/admin',
    name: 'Edison',
    icon: 'crown',
    access: 'canUser3',
    routes: [
      {
        path: '/admin/user3_history',
        name: 'History',
        icon: 'smile',
        component: './user_history/user3_history',
      },
      {
        path: '/admin/user3_prediction',
        name: 'Prediction',
        icon: 'smile',
        component: './user_prediction/user3_prediction',
      },
      {
        component: './404',
      },
    ],
  },
  {
    path: '/admin',
    name: 'Plenitude',
    icon: 'crown',
    access: 'canUser4',
    routes: [
      {
        path: '/admin/user4_history',
        name: 'History',
        icon: 'smile',
        component: './user_history/user4_history',
      },
      {
        path: '/admin/user4_prediction',
        name: 'Prediction',
        icon: 'smile',
        component: './user_prediction/user4_prediction',
      },
      {
        component: './404',
      },
    ],
  }, 
  {
    path: '/admin',
    name: 'Agengranda',
    icon: 'crown',
    access: 'canUser5',
    routes: [
      {
        path: '/admin/user5_history',
        name: 'History',
        icon: 'smile',
        component: './user_history/user5_history',
      },
      {
        path: '/admin/user5_prediction',
        name: 'Prediction',
        icon: 'smile',
        component: './user_prediction/user5_prediction',
      },
      {
        component: './404',
      },
    ],
  },

/*
      {
        name: 'list.table-list',
        icon: 'table',
        path: '/list',
        component: './TableList',
      },
      */
      {
        path: '/',
        redirect: '/welcome',//登陆后显示的界面？
      },
      {
        component: './404',
      },

];
