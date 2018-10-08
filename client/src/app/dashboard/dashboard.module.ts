import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AppModule } from '../app.module';

import { DashboardRoutingModule } from './dashboard-routing.module';
import { DashboardComponent } from './dashboard.component';
import { HeaderComponent } from './header/header.component';
import { LeftPanelComponent } from './left-panel/left-panel.component';
import { MainContentComponent } from './main-content/main-content.component';
// import { Browser } from 'protractor';

@NgModule({
  imports: [
    AppModule,
    CommonModule,
    DashboardRoutingModule
  ],
  // exports: [  ],
  declarations: [DashboardComponent, HeaderComponent, LeftPanelComponent, MainContentComponent]
})
export class DashboardModule { }
