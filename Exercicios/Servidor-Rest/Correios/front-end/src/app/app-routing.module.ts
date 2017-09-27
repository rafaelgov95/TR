import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AuthGuard } from './shared';
const routes: Routes = [
    {
        path: 'dashboard',
        loadChildren: './blog/dashboard/dashboard.module#DashboardModule',
        canActivate: [AuthGuard]
    },
    { path: '', loadChildren: './blog/blog.module#BlogModule' },
    { path: 'post/:id', loadChildren: './blog/blog.module#BlogModule' },
    { path: 'not-found', loadChildren: './not-found/not-found.module#NotFoundModule' },
    { path: '**', redirectTo: 'not-found' }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }
