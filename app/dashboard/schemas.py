#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-09-27 08:14:40
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from app.mixins.commons import ListBase
from pydantic import BaseModel, Field
from typing import Any, Dict, Optional, List

from app.utils.custom_validators import currency_out_val


class RegistrationInfo(BaseModel):
    vehicles_info: Optional[Dict] = Field(None, description="Vehicles Info")
    drivers_info: Optional[Dict] = Field(None, description="Drivers Info")
    total_reg: Optional[int] = Field(None, description="Total Registered vehicle and drivers")


class SuperAdminDashboard(RegistrationInfo):
    pass


class RegAdminDashboard(RegistrationInfo):
    pass


class InternalRevenueDashboard(RegistrationInfo):
    pass


class GovernorDashboard(RegistrationInfo):
    pass


class SuperTaxVendorDashboard(BaseModel):
    wallet_number: Optional[str] = Field(None, description="Wallet Number")
    wallet_balance: Optional[float] = Field(None, description="Wallet Balance")
    total_vendors: Optional[int] = Field(None, description="Total registered vendors")
    total_profit_today: Optional[float] = Field(None, description="Total profit today")
    total_profit: Optional[float] = Field(None, description="Total profit")
    credit_sold_today: Optional[float] = Field(None, description="Total tax sold today")
    credit_sold_total: Optional[float] = Field(None, description="Total tax sold")

    _val_wallet_balance = currency_out_val("wallet_balance")
    _val_total_profit_today = currency_out_val("total_profit_today")
    _val_total_profit = currency_out_val("total_profit")
    _val_total_tax_sold_today = currency_out_val("credit_sold_today")
    _val_total_tax_sold = currency_out_val("credit_sold_total")

class TaxVendorDashboard(BaseModel):
    wallet_number: Optional[str] = Field(None, description="Wallet Number")
    wallet_balance: Optional[float] = Field(None, description="Wallet Balance")
    tax_sold_today: Optional[float] = Field(None, description="Tax Sold Today")
    tax_sold_total: Optional[float] = Field(None, description="Tax Sold Total")
    profit_today: Optional[float] = Field(None, description="Profit Today")
    profit_total: Optional[float] = Field(None, description="Profit Total")

    _val_wallet_balance = currency_out_val("wallet_balance")
    _val_tax_sold_today = currency_out_val("tax_sold_today")
    _val_tax_sold_total = currency_out_val("tax_sold_total")
    _val_profit_today = currency_out_val("profit_today")
    _val_profit_total = currency_out_val("profit_total")


class TaxPaymentSuperAdmin(BaseModel):
    daily_revenue: Optional[float] = Field(None, description="Daily Revenue")
    total_revenue: Optional[float] = Field(None, description="Total Revenue")
    daily_consultant_revenue: Optional[float] = Field(None, description="Daily Consultant Revenue")
    total_consultant_revenue: Optional[float] = Field(None, description="Total Consultant Revenue")
    credit_sold_today: Optional[float] = Field(None, description="Credit Sold Today")
    credit_sold_total: Optional[float] = Field(None, description="Credit Sold Total")


    _val_daily_revenue = currency_out_val("daily_revenue")
    _val_total_revenue = currency_out_val("total_revenue")
    _val_daily_consultant_revenue = currency_out_val("daily_consultant_revenue")
    _val_total_consultant_revenue = currency_out_val("total_consultant_revenue")
    _val_credit_sold_today = currency_out_val("credit_sold_today")
    _val_credit_sold_total = currency_out_val("credit_sold_total")


class TaxPaymentInternalRevenue(BaseModel):
    daily_revenue: Optional[float] = Field(None, description="Daily Revenue")
    total_revenue: Optional[float] = Field(None, description="Total Revenue")

    _val_daily_revenue = currency_out_val("daily_revenue")
    _val_total_revenue = currency_out_val("total_revenue")


class TaxPaymentGovernor(BaseModel):
    daily_revenue: Optional[float] = Field(None, description="Daily Revenue")
    total_revenue: Optional[float] = Field(None, description="Total Revenue")

    _val_daily_revenue = currency_out_val("daily_revenue")
    _val_total_revenue = currency_out_val("total_revenue")


class TaxPaymentAssociationHead(BaseModel):
    daily_revenue: Optional[float] = Field(None, description="Daily Revenue")
    total_revenue: Optional[float] = Field(None, description="Total Revenue")

    _val_daily_revenue = currency_out_val("daily_revenue")
    _val_total_revenue = currency_out_val("total_revenue")

