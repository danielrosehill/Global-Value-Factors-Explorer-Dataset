---
language:
- en
pretty_name: IFVI Value Factors - Derivative Dataset For Analysis
---
![alt text](images/graphics/3.png)

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/danielrosehill/Global-Value-Factors-Explorer-Dataset)  
[![Hugging Face Dataset](https://img.shields.io/badge/Hugging%20Face-Dataset-orange?logo=huggingface)](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv)  
[![Original Data](https://img.shields.io/badge/Original-Data-green)](https://ifvi.org/methodology/environmental-topic-methodology/interim-methodologies/#GlobalValueFactorDatabase)


## 🚀 What if companies' environmental impacts could be quantified in monetary terms!?

<a id="about-the-global-value-factors-explorer-dataset"></a>
## 🌍 About The Global Value Factors Explorer Dataset

The Global Value Factors Database, released by the [International Foundation for Valuing Impacts](https://www.ifvi.org) during UN Climate Week NYC 2023, provides a set of almost 100,000 “value factors” for converting environmental impacts into monetary terms.  

The GVFD covers 430 different environmental impacts across four main categories of impact: air pollution, land use and conversion, waste and water pollution . With the exception of the value factor for greenhouse gas emissions, for which a single value factor is provided ($236/tco2e), the value factors are geographically stratified (in other words, the value factors are both impact-specific and geolocation-specific).  In total, there are 268 geolocations in the dataset reflecting all the world's recognised sovereigns as well as some international dependencies. In addition, one set of value factors, air pollution, provides data at the level of US states. 

# Key Data Parameters

| Parameter             | Value                                                                                               |
|----------------------|---------------------------------------------------------------------------------------------------------------------|
| Value Factors        | Almost 100,000 "value factors" for converting quantitative environmental data into monetary equivalents (USD)          |
| Geolocations         | 268 geolocations (world sovereigns plus US states - for air pollution methodology only)                               |
| Impacts Covered      | Air pollution; GHG emissions; land use and conversion; water use and pollution; waste.                            |
| Parameter Source Data| Global Value Factors Database as released by the International Foundation for Valuing Impacts in September 2024      |
| License              | Licensing in accordance with IFVI, [license link](https://ifvi.org/methodology/environmental-topic-methodology/interim-methodologies/download-form-global-value-factor-database/) |

---

# Impact Categories In Dataset

![alt text](images/graphics/4.png)

 Here is the updated version of the table with an additional **Description** column and the descriptions you provided:

| **Category Name**   | **Description**                                                                                          | **Impacts Considered**                                                                                       | **Reporting Units** | **Geostratified**          |
|----------------------|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|---------------------|-----------------------------|
| Air Pollution        | Impacts caused by air pollution, by location and specific pollutant                                    | Metric tons of PM2.5, PM10, SOx, NOx, NH3, and VOCs per year                                              | Metric tons/year    | Yes (by country and US state) |
| GHG Emissions        | Social costs of GHG emissions                                                                          | Single globally applicable factor of 236 per ton of CO2 equivalent ($/tCO2e)                              | Metric tons/year    | No                          |
| Land Conversion      | Displacement of land from pristine state into land for commercial activities                           | Land use changes in categories such as wheat, oilseeds, forestry, and paved land                          | Hectares (ha)       | Yes                         |
| Land Use             | Ongoing ecosystem loss; cost due to continuing use of land for commercial purposes                     | Types of agriculture (e.g., wheat, oilseeds), forestry, and paved land                                    | Hectares (ha)       | Yes                         |
| Waste                | Adverse effects associated with the generation and disposal of waste                                   | Categorized as hazardous or non-hazardous by disposal method (landfill, incineration, unspecified)         | Kilograms (kg)      | Yes                         |
| Water Consumption    | Factors related to water consumption                                                                   | Factors such as malnutrition, water-borne diseases, resource costs, and ecosystem effects                 | Cubic meters (m³)   | Yes                         |
| Water Pollution      | Impacts caused by polluting water systems divided by pollutant and setting                             | 104 pollutants including phosphorus, nitrogen, heavy metals, pesticides, and pharmaceuticals              | Kilograms (kg)      | Yes                         |

 
---

# Download Links - Value Factors By Methodology (CSV)

| Title               | Format | Link                                                                                                   |
|---------------------|--------|-------------------------------------------------------------------------------------------------------|
| Air Pollution       | CSV    | [![Download](https://img.shields.io/badge/Download-Air_Pollution-blue?style=flat-square)](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/resolve/main/data/csv/by-methodology/airpollution.csv) |
| GHG Emissions       | CSV    | [![Download](https://img.shields.io/badge/Download-GHG_Emissions-blue?style=flat-square)](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/resolve/main/data/csv/by-methodology/ghgs.csv) |
| Land Conversion     | CSV    | [![Download](https://img.shields.io/badge/Download-Land_Conversion-blue?style=flat-square)](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/resolve/main/data/csv/by-methodology/land-conversion.csv) |
| Land Use            | CSV    | [![Download](https://img.shields.io/badge/Download-Land_Use-blue?style=flat-square)](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/resolve/main/data/csv/by-methodology/land-use.csv) |
| Waste               | CSV    | [![Download](https://img.shields.io/badge/Download-Waste-blue?style=flat-square)](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/resolve/main/data/csv/by-methodology/waste.csv) |
| Water Consumption   | CSV    | [![Download](https://img.shields.io/badge/Download-Water_Consumption-blue?style=flat-square)](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/resolve/main/data/csv/by-methodology/water-consumption.csv) |
| Water Pollution     | CSV    | [![Download](https://img.shields.io/badge/Download-Water_Pollution-blue?style=flat-square)](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/resolve/main/data/csv/by-methodology/water-pollution.csv) |


# Download Links - Value Factors By Methodology, By Country (JSON)

Hierarchical JSON representation of value factors: by methodology, by country, then by category, impact and finally to individual factors. 

Okay, here's the table with the added ISO 3166-1 alpha-3 and alpha-2 codes.  I've used a Python script to fetch the codes based on the country names. 

| Country | Continent | Download Link | ISO 3166-1 Alpha-3 | ISO 3166-1 Alpha-2 |
|---------|-----------|---------------|--------------------|--------------------|
| Algeria | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Algeria.json) | DZA | DZ |
| Angola | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Angola.json) | AGO | AO |
| Benin | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Benin.json) | BEN | BJ |
| Botswana | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Botswana.json) | BWA | BW |
| Burkina Faso | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Burkina%20Faso.json) | BFA | BF |
| Burundi | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Burundi.json) | BDI | BI |
| Cabo Verde | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Cabo%20Verde.json) | CPV | CV |
| Cameroon | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Cameroon.json) | CMR | CM |
| Central African Republic | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Central%20African%20Republic.json) | CAF | CF |
| Chad | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Chad.json) | TCD | TD |
| Comoros | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Comoros.json) | COM | KM |
| Democratic Republic of the Congo | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Democratic%20Republic%20of%20the%20Congo.json) | COD | CD |
| Djibouti | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Djibouti.json) | DJI | DJ |
| Egypt | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Egypt.json) | EGY | EG |
| Equatorial Guinea | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Equatorial%20Guinea.json) | GNQ | GQ |
| Eritrea | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Eritrea.json) | ERI | ER |
| Eswatini | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Eswatini.json) | SWZ | SZ |
| Ethiopia | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Ethiopia.json) | ETH | ET |
| Gabon | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Gabon.json) | GAB | GA |
| Gambia | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Gambia.json) | GMB | GM |
| Ghana | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Ghana.json) | GHA | GH |
| Guinea-Bissau | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Guinea-Bissau.json) | GNB | GW |
| Guinea | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Guinea.json) | GIN | GN |
| Kenya | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Kenya.json) | KEN | KE |
| Lesotho | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Lesotho.json) | LSO | LS |
| Liberia | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Liberia.json) | LBR | LR |
| Libya | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Libya.json) | LBY | LY |
| Madagascar | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Madagascar.json) | MDG | MG |
| Malawi | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Malawi.json) | MWI | MW |
| Mali | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Mali.json) | MLI | ML |
| Mauritania | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Mauritania.json) | MRT | MR |
| Mauritius | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Mauritius.json) | MUS | MU |
| Morocco | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Morocco.json) | MAR | MA |
| Mozambique | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Mozambique.json) | MOZ | MZ |
| Namibia | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Namibia.json) | NAM | NA |
| Niger | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Niger.json) | NER | NE |
| Nigeria | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Nigeria.json) | NGA | NG |
| Republic of the Congo | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Republic%20of%20the%20Congo.json) | COG | CG |
| Rwanda | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Rwanda.json) | RWA | RW |
| Sao Tome and Principe | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Sao%20Tome%20and%20Principe.json) | STP | ST |
| Senegal | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Senegal.json) | SEN | SN |
| Seychelles | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Seychelles.json) | SYC | SC |
| Sierra Leone | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Sierra%20Leone.json) | SLE | SL |
| Somalia | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Somalia.json) | SOM | SO |
| South Africa | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/South%20Africa.json) | ZAF | ZA |
| South Sudan | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/South%20Sudan.json) | SSD | SS |
| Sudan | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Sudan.json) | SDN | SD |
| Tanzania | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Tanzania.json) | TZA | TZ |
| Togo | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Togo.json) | TGO | TG |
| Tunisia | Africa | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Africa/Tunisia.json) | TUN | TN |
| Afghanistan | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Afghanistan.json) | AFG | AF |
| Armenia | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Armenia.json) | ARM | AM |
| Azerbaijan | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Azerbaijan.json) | AZE | AZ |
| Bahrain | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Bahrain.json) | BHR | BH |
| Bangladesh | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Bangladesh.json) | BGD | BD |
| Bhutan | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Bhutan.json) | BTN | BT |
| Brunei Darussalam | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Brunei%20Darussalam.json) | BRN | BN |
| Cambodia | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Cambodia.json) | KHM | KH |
| China | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/China.json) | CHN | CN |
| Cyprus | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Cyprus.json) | CYP | CY |
| Georgia | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Georgia.json) | GEO | GE |
| Hong Kong SAR | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Hong%20Kong%20SAR.json) | HKG | HK |
| India | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/India.json) | IND | IN |
| Indonesia | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Indonesia.json) | IDN | ID |
| Iran | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Iran.json) | IRN | IR |
| Iraq | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Iraq.json) | IRQ | IQ |
| Israel | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Israel.json) | ISR | IL |
| Japan | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Japan.json) | JPN | JP |
| Jordan | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Jordan.json) | JOR | JO |
| Kazakhstan | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Kazakhstan.json) | KAZ | KZ |
| Kuwait | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Kuwait.json) | KWT | KW |
| Kyrgyz Republic | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Kyrgyz%20Republic.json) | KGZ | KG |
| Lao | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Lao.json) | LAO | LA |
| Lebanon | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Lebanon.json) | LBN | LB |
| Macao | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Macao.json) | MAC | MO |
| Malaysia | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Malaysia.json) | MYS | MY |
| Maldives | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Maldives.json) | MDV | MV |
| Mongolia | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Mongolia.json) | MNG | MN |
| Myanmar | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Myanmar.json) | MMR | MM |
| Nepal | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Nepal.json) | NPL | NP |
| North Korea | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/North%20Korea.json) | PRK | KP |
| Oman | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Oman.json) | OMN | OM |
| Pakistan | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Pakistan.json) | PAK | PK |
| Philippines | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Philippines.json) | PHL | PH |
| Qatar | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Qatar.json) | QAT | QA |
| Saudi Arabia | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Saudi%20Arabia.json) | SAU | SA |
| Singapore | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Singapore.json) | SGP | SG |
| South Korea | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/South%20Korea.json) | KOR | KR |
| Sri Lanka | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Sri%20Lanka.json) | LKA | LK |
| Syria | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Syria.json) | SYR | SY |
| Taiwan | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Taiwan.json) | TWN | TW |
| Tajikistan | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Tajikistan.json) | TJK | TJ |
| Thailand | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Thailand.json) | THA | TH |
| Timor-Leste | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Timor-Leste.json) | TLS | TL |
| Turkiye | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Turkiye.json) | TUR | TR |
| Turkmenistan | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Turkmenistan.json) | TKM | TM |
| United Arab Emirates | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/United%20Arab%20Emirates.json) | ARE | AE |
| Uzbekistan | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Uzbekistan.json) | UZB | UZ |
| Vietnam | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/Vietnam.json) | VNM | VN |
| West Bank and Gaza | Asia | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Asia/West%20Bank%20and%20Gaza.json) | PSE | PS |
| Albania | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Albania.json) | ALB | AL |
| Andorra | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Andorra.json) | AND | AD |
| Austria | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Austria.json) | AUT | AT |
| Belarus | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Belarus.json) | BLR | BY |
| Belgium | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Belgium.json) | BEL | BE |
| Bosnia and Herzegovina | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Bosnia%20and%20Herzegovina.json) | BIH | BA |
| Bulgaria | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Bulgaria.json) | BGR | BG |
| Channel Islands | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Channel%20Islands.json) |  |  |
| Croatia | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Croatia.json) | HRV | HR |
| Czechia | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Czechia.json) | CZE | CZ |
| Denmark | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Denmark.json) | DNK | DK |
| Estonia | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Estonia.json) | EST | EE |
| Faroe Islands | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Faroe%20Islands.json) | FRO | FO |
| Finland | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Finland.json) | FIN | FI |
| France | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/France.json) | FRA | FR |
| Germany | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Germany.json) | DEU | DE |
| Gibraltar | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Gibraltar.json) | GIB | GI |
| Greece | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Greece.json) | GRC | GR |
| Greenland | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Greenland.json) | GRL | GL |
| Hungary | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Hungary.json) | HUN | HU |
| Iceland | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Iceland.json) | ISL | IS |
| Ireland | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Ireland.json) | IRL | IE |
| Isle of Man | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Isle%20of%20Man.json) | IMN | IM |
| Italy | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Italy.json) | ITA | IT |
| Kosovo | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Kosovo.json) |  |  |
| Latvia | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Latvia.json) | LVA | LV |
| Liechtenstein | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Liechtenstein.json) | LIE | LI |
| Lithuania | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Lithuania.json) | LTU | LT |
| Luxembourg | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Luxembourg.json) | LUX | LU |
| Malta | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Malta.json) | MLT | MT |
| Moldova | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Moldova.json) | MDA | MD |
| Monaco | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Monaco.json) | MCO | MC |
| Montenegro | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Montenegro.json) | MNE | ME |
| Netherlands | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Netherlands.json) | NLD | NL |
| North Macedonia | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/North%20Macedonia.json) | MKD | MK |
| Norway | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Norway.json) | NOR | NO |
| Poland | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Poland.json) | POL | PL |
| Portugal | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Portugal.json) | PRT | PT |
| Romania | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Romania.json) | ROU | RO |
| Russian Federation | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Russian%20Federation.json) | RUS | RU |
| San Marino | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/San%20Marino.json) | SMR | SM |
| Serbia | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Serbia.json) | SRB | RS |
| Slovak Republic | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Slovak%20Republic.json) | SVK | SK |
| Slovenia | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Slovenia.json) | SVN | SI |
| Spain | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Spain.json) | ESP | ES |
| Sweden | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Sweden.json) | SWE | SE |
| Switzerland | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Switzerland.json) | CHE | CH |
| Ukraine | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/Ukraine.json) | UKR | UA |
| United Kingdom | Europe | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Europe/United%20Kingdom.json) | GBR | GB |
| Antigua and Barbuda | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Antigua%20and%20Barbuda.json) | ATG | AG |
| Aruba | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Aruba.json) | ABW | AW |
| Bahamas | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Bahamas.json) | BHS | BS |
| Barbados | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Barbados.json) | BRB | BB |
| Belize | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Belize.json) | BLZ | BZ |
| Bermuda | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Bermuda.json) | BMU | BM |
| British Virgin Islands | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/British%20Virgin%20Islands.json) | VGB | VG |
| Canada | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Canada.json) | CAN | CA |
| Cayman Islands | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Cayman%20Islands.json) | CYM | KY |
| Costa Rica | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Costa%20Rica.json) | CRI | CR |
| Cuba | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Cuba.json) | CUB | CU |
| Curacao | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Curacao.json) | CUW | CW |
| Dominica | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Dominica.json) | DMA | DM |
| Dominican Republic | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Dominican%20Republic.json) | DOM | DO |
| El Salvador | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/El%20Salvador.json) | SLV | SV |
| Grenada | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Grenada.json) | GRD | GD |
| Guatemala | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Guatemala.json) | GTM | GT |
| Haiti | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Haiti.json) | HTI | HT |
| Honduras | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Honduras.json) | HND | HN |
| Jamaica | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Jamaica.json) | JAM | JM |
| Mexico | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Mexico.json) | MEX | MX |
| Nicaragua | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Nicaragua.json) | NIC | NI |
| Panama | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Panama.json) | PAN | PA |
| Puerto Rico | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Puerto%20Rico.json) | PRI | PR |
| St. Kitts and Nevis | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/St.%20Kitts%20and%20Nevis.json) | KNA | KN |
| St. Lucia | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/St.%20Lucia.json) | LCA | LC |
| St. Maarten (Dutch part) | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/St.%20Maarten%20(Dutch%20part).json) | SXM | SX |
| St. Martin (French part) | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/St.%20Martin%20(French%20part).json) | MAF | MF |
| St. Vincent and the Grenadines | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/St.%20Vincent%20and%20the%20Grenadines.json) | VCT | VC |
| Trinidad and Tobago | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Trinidad%20and%20Tobago.json) | TTO | TT |
| Turks and Caicos Islands | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Turks%20and%20Caicos%20Islands.json) | TCA | TC |
| United States | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/United%20States.json) | USA | US |
| Virgin Islands (U.S.) | North America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/North%20America/Virgin%20Islands%20(U.S.).json) | VIR | VI |
| American Samoa | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/American%20Samoa.json) | ASM | AS |
| Australia | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/Australia.json) | AUS | AU |
| Fiji | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/Fiji.json) | FJI | FJ |
| French Polynesia | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/French%20Polynesia.json) | PYF | PF |
| Guam | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/Guam.json) | GUM | GU |
| Kiribati | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/Kiribati.json) | KIR | KI |
| Marshall Islands | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/Marshall%20Islands.json) | MHL | MH |
| Micronesia | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/Micronesia.json) | FSM | FM |
| Nauru | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/Nauru.json) | NRU | NR |
| New Caledonia | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/New%20Caledonia.json) | NCL | NC |
| New Zealand | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/New%20Zealand.json) | NZL | NZ |
| Northern Mariana Islands | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/Northern%20Mariana%20Islands.json) | MNP | MP |
| Palau | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/Palau.json) | PLW | PW |
| Papua New Guinea | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/Papua%20New%20Guinea.json) | PNG | PG |
| Samoa | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/Samoa.json) | WSM | WS |
| Solomon Islands | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/Solomon%20Islands.json) | SLB | SB |
| Tonga | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/Tonga.json) | TON | TO |
| Tuvalu | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/Tuvalu.json) | TUV | TV |
| Vanuatu | Oceania | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/Oceania/Vanuatu.json) | VUT | VU |
| Argentina | South America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/South%20America/Argentina.json) | ARG | AR |
| Bolivia | South America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/South%20America/Bolivia.json) | BOL | BO |
| Brazil | South America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/South%20America/Brazil.json) | BRA | BR |
| Chile | South America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/South%20America/Chile.json) | CHL | CL |
| Colombia | South America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/South%20America/Colombia.json) | COL | CO |
| Ecuador | South America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/South%20America/Ecuador.json) | ECU | EC |
| Guyana | South America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/South%20America/Guyana.json) | GUY | GY |
| Paraguay | South America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/South%20America/Paraguay.json) | PRY | PY |
| Peru | South America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/South%20America/Peru.json) | PER | PE |
| Suriname | South America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/South%20America/Suriname.json) | SUR | SR |
| Uruguay | South America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/South%20America/Uruguay.json) | URY | UY |
| Venezuela | South America | [Download](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv/blob/main/data/by-territory/by-continent/South%20America/Venezuela.json) | VEN | VE |

---

# Links To Supporting Documents And Guides, IFVI Website

Please note:

These links were aggregated on 20/12/24. 

The IFVI's consultative processes are ongoing and these links may change in the future. 

For the latest versions of the interim methodologies, comment forms, and technical manuals refer to the IFVI website at [ifvi.org](https://www.ifvi.org)

# GHG Emissions Methodology

| Title                     | Link                                                                                  |
|---------------------------|---------------------------------------------------------------------------------------|
| Methodology Paper         | [![Open Link](https://img.shields.io/badge/Open-Link-blue)](https://share.hsforms.com/1yn-WjRi3SbqxEBKPesJ-Kwqaucq) |
| Implementation Guide      | [![Open Link](https://img.shields.io/badge/Open-Link-blue)](https://ifvi.org/wp-content/uploads/2024/11/IFVI-VBA_GHG_-Implementation-Guide.pdf) |
| Basis For Conclusions     | [![Open Link](https://img.shields.io/badge/Open-Link-blue)](https://ifvi.org/wp-content/uploads/2024/09/IFVI_VBA_Environmental-Methodology-1_GHG-Topic-Methodology_Basis-for-Conclusions.pdf) |

# Water Consumption Methodology

| Title                                     | Link                                                                                  |
|-------------------------------------------|---------------------------------------------------------------------------------------|
| Exposure Draft                            | [![Open Link](https://img.shields.io/badge/Open-Link-blue)](https://ifvi.org/wp-content/uploads/2024/09/IFVI_VBA_Exposure-DRAFT_Water-Consumption-Topic-Methodology.pdf) |
| Public Comment Feedback Summary (XLSX)   | [![Open Link](https://img.shields.io/badge/Open-Link-blue)](https://ifvi.org/wp-content/uploads/2024/12/IFVI_VBA_Public-Comment-Feedback_Water-Consumption-Topic-Methodology.xlsx) |

# Other Methodologies

| Title                                     | Link                                                                                  |
|-------------------------------------------|---------------------------------------------------------------------------------------|
| Download form for methodologies           | [![Open Link](https://img.shields.io/badge/Open-Link-blue)](https://ifvi.org/methodology/environmental-topic-methodology/interim-methodologies/download-form-interim-methodology/) |
| Download form for models and technical manuals | [![Open Link](https://img.shields.io/badge/Open-Link-blue)](https://ifvi.org/methodology/environmental-topic-methodology/interim-methodologies/download-form-interim-models-and-technical-manuals/) |

---

# Value Factors - Use Case Descriptions

## Impact Accounting

![alt text](images/graphics/1.png)

The value factors are intended for use by account preparers preparing financial statements which integrate their environmental and social impacts alongside their traditional financial impacts, unifying all their holistic impacts into one set of financial calculations  While the GVFD covers only environmental factors, a key part of the IFVI's mission is also developing methodologies for quantifying social impacts. 

 In order to fulfill their intended purpose, the value factors need to be matched with the raw quantitative environmental data which each value factor is intended to convert into monetary terms (the value factors are expressed as conversions to the US dollar).

 ## Additional Use-Cases

 Note:
 
 The following suggested additional use cases were authored by me and do not bear the formal endorsement of IFVI. 
 
 Rather, my intention in sharing them is to stimulate thought into how the iterative process of arriving at methods of converting environmental data into monetary terms could have uses beyond impact accounting. This list is extremely non-exhaustive and many more potential interesting uses for this data can be suggested.

| **Use Case**                              | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tax Credits                              | The value factors could provide a framework for governments to devise and implement incentives to encourage companies to a) implement robust strategies around the collection and measurement of environmental parameters, and b) encourage those doing so with reduced taxation, which could also be used to offset the cost of collection programs.                                                                                                             |
| Comparing Financial Performance And Sustainability | There is vigorous interest from a wide variety of stakeholders in understanding the extent to which companies' environmental performance and profitability are correlated. This analysis is enabled by having a diverse range of environmental parameters that can be monetized. Given the significant variability in the environmental parameters that publicly traded companies collect and disclose, a broad array of “value factors” is particularly advantageous, as it increases the likelihood that a meaningful amount of data will be available for any given reporter. Impact accounting involves the direct integration of these value factors by account preparers; however, it is equally important for external entities, such as sector analysts and environmental lobby groups, to use these factors to create composites of financial and sustainability reporting by applying them to publicly released financial data. Publicly traded companies inherently release financial data, and an increasing number also consistently publish sustainability data in quantitative terms. Value factors serve as a bridge between these two datasets, enabling even approximations of the theorized financial effects of environmental impacts to be assessed and considered. |
| Policy Formulation                        | In our current economic system, companies are often recused from financially contributing to mitigate environmental impacts attributed to them. Given scarce public resources and fairness concerns, many argue companies should act as financial participants in these programs. Monetizing their environmental impacts could provide a “bill” for companies' financial effects, aiding in policy arguments and garnering support for corporate responsibility as a true obligation rather than voluntary action.                              |

 # About This Data Project (Derivative Database)

 ![alt text](images/graphics/3.png)

This derivative dataset was prepared by me, Daniel Rosehill, in order to facilitate the exploration and analysis of this dataset by non-commercial users.  I believe that there is a strong policy interest in the question of how companies' impacts can be properly accounted for, recognising their societal and planetary effects. 

To facilitate such analysis, I undertook a data reformatting process converting the initial version of the IFVI data from its original format (`XLSM`) and providing it as extracted comma-separated value files, as well as `JSON` structured in various hierarchies, some reflecting a territorial hierarchy (i.e. by geolocation) and others reflecting an impact-first hierarchy (in other words, with the impacts as the primary level, and the geo-stratified value factors nested under them). 

The CSV files should provide the flexibility for users to work with the data as they see fit, while the `JSON` files direct towards specific vantage points and use cases for the data. 

Use of the value factors is governed in accordance with the licensing terms provided by the IFVI (which, at the time of writing, provide for free usage for individual account preparers and non-commercial users.) Those looking to read the full official licence should refer to the website of the IFVI at www.ifvi.org 

 ## 📜 Licensing

This derivative dataset is subject to the same terms of use as the original database, available in `license.md` at the repository root. These licensing conditions are stipulated by the International Foundation for Valuing Impacts. At the time of writing, the licensing terms provide for wide use of the data on a complimentary basis (including by account preparers) with limited exclusions to that position for those looking to integrate the data into commercial data products for which licensing charges apply. Questions regarding licensing of the database and requests for clarification regarding allowable uses and any other queries regarding compliance with the terms of their license should be referred to the IFVI.

## 📅 Versioning

This repository reflects GVFD Version 1 (October 15th, 2024).  It is not guaranteed to be the most recent version.  Consult the IFVI website for the latest data and updates.  While this repository aims to mirror the original GVFD, using this data for official purposes requires referencing the complete IFVI documentation, which is not included here.

<a id="data-formatting"></a>
## 🗂️ Data Formatting

The source data has been restructured for various analytical perspectives:

 | **Data Category**            | **Description**                                                                                   |
|-------------------------------|---------------------------------------------------------------------------------------------------|
| **By Methodology**            | JSON arrays organized by methodology parameters.                                                 |
| **By Methodology, By Country**| Mirrors the source database structure (except Land Use and Conversion, which are split into two files). |
| **By Territory**              | Organizes data geographically by continent, territory, and US state (US states appear in one methodology). JSON files aggregate data from various methodology tabs. |

Additional resources:

* CSV format data.
* `metadata/` folder containing non-data items (e.g., notes from the original database tabs).

<a id="data-modifications"></a>
## 🛠️ Data Modifications

No material data changes were made.  Modifications are limited to formatting and restructuring for analysis.  Two non-material changes (documented in the changelog) are:

* Removal of US dollar signs for easier database integration.
* Standardization of 12 country names to more common versions (e.g., "Bahamas, The" to "Bahamas") and mapping all territories to their ISO-3166 Alpha-2 codes for clarity.

<a id="release-notes-for-v2"></a>

---

# 📝 Release Notes For V2

This release standardises versioning for an early iteration (V2) of the derivative database of the [IFVI Global Value Factors Database (GVFD)](https://ifvi.org/methodology/environmental-topic-methodology/interim-methodologies/).

This package consists of `JSON` representations of the original `XLSM` database contained in the original IFVI data release.

### JSON hierarchies reflecting different organisations of the source data

The data tables in this derivative dataset are organised into various hierarchies to support different data analytics and visualisation use-cases:

- `by-methodology` This folder is divided into subfolders tracking the various methodologies used by the IFVI. The files it contains are "custom" (original) hierarchies representing the data. Not all the methodologies have data tables in this folder.
- `by-methodology-by-country` This folder maps most closely onto the original format in which the data was released and divides the database firstly by methodology and then by country (and then with impacts, values, etc)
- `by-territory` This folder consists of individual JSON files for the various countries and territories (including US states) that were included in some or all of the methodology data releases. The datasets here are organised firstly into geographical continents and then by country (or territory; some of the territories are not widely recognised as independent sovereigns). US states - which were included in one methodology - have their own subfolder.

## Data Modifications (Non-Substantive)

This dataset (and the repository containing it) is a non-official derivative of the International Foundation for Valuing Impact (IFVI) Global Value Factors Database (GVFD) V1.  This derivative dataset is intended to support the programmatic use of the Database for research-related analysis and visualisation. 

This dataset intends to reflect an accurate reformatting of the source data at the time of its compilation. This version of the derivative dataset is based upon the first version of the GVFD as published by the IFVI on October 15th 2024.

No material edits have been made to the source data. 

The following edits were made solely to support the intended use-case:

## Removal of currency symbols

To streamline intake of these `JSON` files into database systems, non-integer data (currency symbols) were scrubbed from the dataset. As is noted in the metadata, the IFVI Database is standardised on the US Dollar. 

## Editing of country and territory names

To assist with geovisualisation use-cases, all countries and territories were matched with their corresponding `alpha-2` values as defined by `ISO 3166`,

In order to render the names of countries and territories in more easily recognisable formatting, the names of 18 countries and territories were lightly reformatted. 

For example `"Bahamas, The"` was renamed `"Bahamas"` and `"Egypt, Arab Rep."` was renamed as simply `"Egypt."` 


## Separation Of Non-Data Entities 

- `metadata` This folder provides individual JSONs which capture the notes that were appended on each tab of the source `XLSM`
- `reference` A static snapshot of the supporting documentation (methodologies and user manuals) released by the IFVI alongside the data release

---

# Data Parameters By Impact Category

#### Air Pollution: Data Description

| **Title**               | **Details**                                                                                                                                                                                                                                           |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Dataset Name**        | Air Pollution Methodology                                                                                                                                                                                                                             |
| **Methodology Status**  | Interim                                                                                                                                                                                                                                              |
| **Location-sensitive?** | Yes                                                                                                                                                                                                                                                  |
| **Territories provided**| 197 countries, 51 US states/territories (including Washington, D.C.)                                                                                                                                            |
| **Example parameters**  | PM2.5, PM10, SOx, NOx, NH3, VOC                                                                                                                                                                                                                      |
| **Units**               | Metric tons per year (per pollutant)                                                                                                                                                                                                                  |
| **Sample datapoint**    | Air Pollution_PM2.5_Urban_Primary Health                                                                                                                                                                                                             |

#### GHG Emissions: Data Description

| **Title**               | **Details**                                                                                                                                                                                                                                           |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Dataset Name**        | GHG Methodology                                                                                                                                                                                                                                       |
| **Methodology Status**  | Interim                                                                                                                                                                                                                                              |
| **Location-sensitive?** | No                                                                                                                                                                                                                                                   |
| **Territories provided**| N/A                                                                                                                                                                                                                                                  |
| **Example parameters**  | Global warming potential, carbon dioxide equivalency                                                                                                                                                                                                  |
| **Units**               | $/tCO2e (USD per metric ton of CO2 equivalent)                                                                                                                                                                                                       |
| **Sample datapoint**    | 236.0 $/tCO2e                                                                                                                                                                                                                                        |

#### Land Conversion: Data Description

| **Title**               | **Details**                                                                                                                                                                                                                                           |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Dataset Name**        | Land Conversion Methodology                                                                                                                                                                                                                           |
| **Methodology Status**  | Interim                                                                                                                                                                                                                                              |
| **Location-sensitive?** | Yes                                                                                                                                                                                                                                                  |
| **Territories provided**| 197 countries                                                                                                                                                                                                                                        |
| **Example parameters**  | Wheat - conventional, Oilseeds - conventional, Cashmere - sustainable, Forestry, Paved                                                                                                                                                                |
| **Units**               | Hectares (for land use categories)                                                                                                                                                                                                                    |
| **Sample datapoint**    | Land Conversion_Wheat - conventional_Lost Ecosystem Services                                                                                                                                                                                          |

#### Land Use: Data Description:

| **Title**               | **Details**                                                                                                                                                                                                                                           |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Dataset Name**        | Land Use Methodology                                                                                                                                                                                                                                  |
| **Methodology Status**  | Interim                                                                                                                                                                                                                                              |
| **Location-sensitive?** | Yes                                                                                                                                                                                                                                                  |
| **Territories provided**| 197 countries                                                                                                                                                                                                                                        |
| **Example parameters**  | Wheat - conventional, Oilseeds - conventional, Cashmere - sustainable, Forestry, Paved                                                                                                                                                                |
| **Units**               | Hectares (ha)                                                                                                                                                                                                                                         |
| **Sample datapoint**    | Land Use_Wheat - conventional_Lost Ecosystem Services                                                                                                                                                                                                |

#### Waste: Data Description

| **Title**               | **Details**                                                                                                                                                                                                                                           |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Dataset Name**        | Waste Methodology                                                                                                                                                                                                                                     |
| **Methodology Status**  | Interim                                                                                                                                                                                                                                              |
| **Location-sensitive?** | Yes                                                                                                                                                                                                                                                  |
| **Territories provided**| 197 countries                                                                                                                                                                                                                                        |
| **Example parameters**  | Hazardous, Non-Hazardous; disposal methods: Landfill, Incineration, Unspecified                                                                                                                                                                       |
| **Units**               | Kilograms (kg)                                                                                                                                                                                                                                        |
| **Sample datapoint**    | Waste_Hazardous_Landfill_Leachate                                                                                                                                                                                                                    |

#### Water Consumption: Data Description:

| **Title**               | **Details**                                                                                                                                                                                                                                           |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Dataset Name**        | Water Consumption Methodology                                                                                                                                                                                                                         |
| **Methodology Status**  | Interim                                                                                                                                                                                                                                              |
| **Location-sensitive?** | No                                                                                                                                                                                                                                                   |
| **Territories provided**| 197 countries                                                                                                                                                                                                                                        |
| **Example parameters**  | Malnutrition, Water-borne disease, Resource cost, Ecosystem services                                                                                                                                                                                  |
| **Units**               | Cubic meters (m³)                                                                                                                                                                                                                                     |
| **Sample datapoint**    | Water Consumption_N/A for WC_N/A for WC_Malnutrition                                                                                                                                                                                                 |

#### Water Pollution: Data Description:

| **Title**               | **Details**                                                                                                                                                                                                                                           |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Dataset Name**        | Water Pollution Methodology                                                                                                                                                                                                                           |
| **Methodology Status**  | Interim                                                                                                                                                                                                                                              |
| **Location-sensitive?** | Yes                                                                                                                                                                                                                                                  |
| **Territories provided**| 197 countries                                                                                                                                                                                                                                        |
| **Example parameters**  | Phosphorus, Nitrogen, Heavy Metals (e.g., Cadmium, Lead, Mercury), Pesticides, Pharmaceuticals (e.g., Antibiotics, NSAIDs)                                                                                                                            |
| **Units**               | Kilograms (kg)                                                                                                                                                                                                                                        |
| **Sample datapoint**    | Water Pollution_Phosphorus_N/A for this Category_Eutrophication                                                                                                                                                                                       |

# Sample Data Values By Methodology

<a id="sample-data"></a>
## 🧪 Sample Data

### Air Pollution

```csv
Country,Category,Location,Impact,Units,Reference,Value
Afghanistan,PM2.5,Urban,Primary Health,/metric ton,Air Pollution_PM2.5_Urban_Primary Health,"40,495.28"
Afghanistan,PM2.5,Peri-Urban,Primary Health,/metric ton,Air Pollution_PM2.5_Peri-Urban_Primary Health,"34,468.58"
Afghanistan,PM2.5,Rural,Primary Health,/metric ton,Air Pollution_PM2.5_Rural_Primary Health,"19,386.52"
Afghanistan,PM2.5,Transport,Primary Health,/metric ton,Air Pollution_PM2.5_Transport_Primary Health,"31,346.36"
Afghanistan,PM2.5,N/A for PM2.5,Visibility,/metric ton,Air Pollution_PM2.5_N/A for PM2.5_Visibility,4.78
Afghanistan,SOx,Urban,Primary Health,/metric ton,Air Pollution_SOx_Urban_Primary Health,"13,398.15"
Afghanistan,SOx,Peri-Urban,Primary Health,/metric ton,Air Pollution_SOx_Peri-Urban_Primary Health,"13,345.45"
Afghanistan,SOx,Rural,Primary Health,/metric ton,Air Pollution_SOx_Rural_Primary Health,"6,694.38"
Afghanistan,SOx,Transport,Primary Health,/metric ton,Air Pollution_SOx_Transport_Primary Health,"10,893.71"
Afghanistan,SOx,N/A for SOx,Visibility,/metric ton,Air Pollution_SOx_N/A for SOx_Visibility,31.86
Afghanistan,NH3,Urban,Primary Health,/metric ton,Air Pollution_NH3_Urban_Primary Health,"12,148.59"
Afghanistan,NH3,Peri-Urban,Primary Health,/metric ton,Air Pollution_NH3_Peri-Urban_Primary Health,"10,340.57"
Afghanistan,NH3,Rural,Primary Health,/metric ton,Air Pollution_NH3_Rural_Primary Health,"5,815.95"
Afghanistan,NH3,Transport,Primary Health,/metric ton,Air Pollution_NH3_Transport_Primary Health,"9,403.91"
Afghanistan,NH3,N/A for NH3,Visibility,/metric ton,Air Pollution_NH3_N/A for NH3_Visibility,6.06
Afghanistan,PM10,Urban,Primary Health,/metric ton,Air Pollution_PM10_Urban_Primary Health,260.51
Afghanistan,PM10,Peri-Urban,Primary Health,/metric ton,Air Pollution_PM10_Peri-Urban_Primary Health,238.92
Afghanistan,PM10,Rural,Primary Health,/metric ton,Air Pollution_PM10_Rural_Primary Health,120.84
```

### Land Conversion

```
Country,Category,Location,Impact,Units,Reference,Value
Afghanistan,Wheat - conventional,N/A for LULC,Lost Ecosystem Services,/ha,Land Conversion_Wheat - conventional_N/A for LULC_Lost Ecosystem Services,"12,573.76"
Afghanistan,"Vegetables, fruit, nuts - conventional",N/A for LULC,Lost Ecosystem Services,/ha,"Land Conversion_Vegetables, fruit, nuts - conventional_N/A for LULC_Lost Ecosystem Services","14,424.09"
Afghanistan,"Cereals, grains - conventional",N/A for LULC,Lost Ecosystem Services,/ha,"Land Conversion_Cereals, grains - conventional_N/A for LULC_Lost Ecosystem Services","12,573.76"
Afghanistan,Oilseeds - conventional,N/A for LULC,Lost Ecosystem Services,/ha,Land Conversion_Oilseeds - conventional_N/A for LULC_Lost Ecosystem Services,"12,573.76"
Afghanistan,"Sugarcane, sugarbeet - conventional",N/A for LULC,Lost Ecosystem Services,/ha,"Land Conversion_Sugarcane, sugarbeet - conventional_N/A for LULC_Lost Ecosystem Services","12,573.76"
Afghanistan,Plant-based fibers - conventional,N/A for LULC,Lost Ecosystem Services,/ha,Land Conversion_Plant-based fibers - conventional_N/A for LULC_Lost Ecosystem Services,"12,573.76"
Afghanistan,Other crops - conventional,N/A for LULC,Lost Ecosystem Services,/ha,Land Conversion_Other crops - conventional_N/A for LULC_Lost Ecosystem Services,"12,573.76"
Afghanistan,Other crops - organic,N/A for LULC,Lost Ecosystem Services,/ha,Land Conversion_Other crops - organic_N/A for LULC_Lost Ecosystem Services,"11,640.73"
Afghanistan,Other crops - sustainable,N/A for LULC,Lost Ecosystem Services,/ha,Land Conversion_Other crops - sustainable_N/A for LULC_Lost Ecosystem Services,"10,870.67"
Afghanistan,"Bovine, sheep, goats, horses - conventional",N/A for LULC,Lost Ecosystem Services,/ha,"Land Conversion_Bovine, sheep, goats, horses - conventional_N/A for LULC_Lost Ecosystem Services","14,200.25"
Afghanistan,"Bovine, sheep, goats, horses - organic",N/A for LULC,Lost Ecosystem Services,/ha,"Land Conversion_Bovine, sheep, goats, horses - organic_N/A for LULC_Lost Ecosystem Services","13,676.30"
Afghanistan,"Bovine, sheep, goats, horses - sustainable",N/A for LULC,Lost Ecosystem Services,/ha,"Land Conversion_Bovine, sheep, goats, horses - sustainable_N/A for LULC_Lost Ecosystem Services","13,521.12"
Afghanistan,Cashmere - conventional,N/A for LULC,Lost Ecosystem Services,/ha,Land Conversion_Cashmere - conventional_N/A for LULC_Lost Ecosystem Services,"14,724.20"
Afghanistan,Cashmere - organic,N/A for LULC,Lost Ecosystem Services,/ha,Land Conversion_Cashmere - organic_N/A for LULC_Lost Ecosystem Services,"13,676.30"
Afghanistan,Cashmere - sustainable,N/A for LULC,Lost Ecosystem Services,/ha,Land Conversion_Cashmere - sustainable_N/A for LULC_Lost Ecosystem Services,"13,521.12"
Afghanistan,Forestry,N/A for LULC,Lost Ecosystem Services,/ha,Land Conversion_Forestry_N/A for LULC_Lost Ecosystem Services,"1,441.78"
Afghanistan,Paddy rice,N/A for LULC,Lost Ecosystem Services,/ha,Land Conversion_Paddy rice_N/A for LULC_Lost Ecosystem Services,"10,984.10"
```

### Land Use

```
Country,Category,Location,Impact,Units,Reference,Value
Afghanistan,Wheat - conventional,N/A for LULC,Lost Ecosystem Services,/ha,Land Use_Wheat - conventional_N/A for LULC_Lost Ecosystem Services,216.64
Afghanistan,"Vegetables, fruit, nuts - conventional",N/A for LULC,Lost Ecosystem Services,/ha,"Land Use_Vegetables, fruit, nuts - conventional_N/A for LULC_Lost Ecosystem Services",248.52
Afghanistan,"Cereals, grains - conventional",N/A for LULC,Lost Ecosystem Services,/ha,"Land Use_Cereals, grains - conventional_N/A for LULC_Lost Ecosystem Services",216.64
Afghanistan,Oilseeds - conventional,N/A for LULC,Lost Ecosystem Services,/ha,Land Use_Oilseeds - conventional_N/A for LULC_Lost Ecosystem Services,216.64
Afghanistan,"Sugarcane, sugarbeet - conventional",N/A for LULC,Lost Ecosystem Services,/ha,"Land Use_Sugarcane, sugarbeet - conventional_N/A for LULC_Lost Ecosystem Services",216.64
Afghanistan,Plant-based fibers - conventional,N/A for LULC,Lost Ecosystem Services,/ha,Land Use_Plant-based fibers - conventional_N/A for LULC_Lost Ecosystem Services,216.64
Afghanistan,Other crops - conventional,N/A for LULC,Lost Ecosystem Services,/ha,Land Use_Other crops - conventional_N/A for LULC_Lost Ecosystem Services,216.64
Afghanistan,Other crops - organic,N/A for LULC,Lost Ecosystem Services,/ha,Land Use_Other crops - organic_N/A for LULC_Lost Ecosystem Services,200.56
Afghanistan,Other crops - sustainable,N/A for LULC,Lost Ecosystem Services,/ha,Land Use_Other crops - sustainable_N/A for LULC_Lost Ecosystem Services,187.3
Afghanistan,"Bovine, sheep, goats, horses - conventional",N/A for LULC,Lost Ecosystem Services,/ha,"Land Use_Bovine, sheep, goats, horses - conventional_N/A for LULC_Lost Ecosystem Services",244.66
Afghanistan,"Bovine, sheep, goats, horses - organic",N/A for LULC,Lost Ecosystem Services,/ha,"Land Use_Bovine, sheep, goats, horses - organic_N/A for LULC_Lost Ecosystem Services",235.64
Afghanistan,"Bovine, sheep, goats, horses - sustainable",N/A for LULC,Lost Ecosystem Services,/ha,"Land Use_Bovine, sheep, goats, horses - sustainable_N/A for LULC_Lost Ecosystem Services",232.96
Afghanistan,Cashmere - conventional,N/A for LULC,Lost Ecosystem Services,/ha,Land Use_Cashmere - conventional_N/A for LULC_Lost Ecosystem Services,253.69
Afghanistan,Cashmere - organic,N/A for LULC,Lost Ecosystem Services,/ha,Land Use_Cashmere - organic_N/A for LULC_Lost Ecosystem Services,235.64
Afghanistan,Cashmere - sustainable,N/A for LULC,Lost Ecosystem Services,/ha,Land Use_Cashmere - sustainable_N/A for LULC_Lost Ecosystem Services,232.96
Afghanistan,Forestry,N/A for LULC,Lost Ecosystem Services,/ha,Land Use_Forestry_N/A for LULC_Lost Ecosystem Services,24.84
Afghanistan,Paddy rice,N/A for LULC,Lost Ecosystem Services,/ha,Land Use_Paddy rice_N/A for LULC_Lost Ecosystem Services,189.25
Afghanistan,Paved,N/A for LULC,Lost Ecosystem Services,/ha,Land Use_Paved_N/A for LULC_Lost Ecosystem Services,312.21
```

### Waste

```
Country,Category,Location,Impact,Units,Reference,Value
Afghanistan,Hazardous,Landfill,Leachate,/kg,Waste_Hazardous_Landfill_Leachate,18.19
Afghanistan,Hazardous,Landfill,Waste GHGs,/kg,Waste_Hazardous_Landfill_Waste GHGs,179.15
Afghanistan,Hazardous,Landfill,Disamenity,/kg,Waste_Hazardous_Landfill_Disamenity,45.96
Afghanistan,Non-Hazardous,Landfill,Leachate,/kg,Waste_Non-Hazardous_Landfill_Leachate,0.3
Afghanistan,Non-Hazardous,Landfill,Waste GHGs,/kg,Waste_Non-Hazardous_Landfill_Waste GHGs,179.15
Afghanistan,Non-Hazardous,Landfill,Disamenity,/kg,Waste_Non-Hazardous_Landfill_Disamenity,45.96
Afghanistan,Hazardous,Incineration,Waste GHGs,/kg,Waste_Hazardous_Incineration_Waste GHGs,386.36
Afghanistan,Hazardous,Incineration,Disamenity,/kg,Waste_Hazardous_Incineration_Disamenity,3.01
Afghanistan,Hazardous,Incineration,Waste Air pollution,/kg,Waste_Hazardous_Incineration_Waste Air pollution,18.28
Afghanistan,Hazardous,Incineration,Heavy metals and dioxins,/kg,Waste_Hazardous_Incineration_Heavy metals and dioxins,4.93
Afghanistan,Non-Hazardous,Incineration,Waste GHGs,/kg,Waste_Non-Hazardous_Incineration_Waste GHGs,124.02
Afghanistan,Non-Hazardous,Incineration,Disamenity,/kg,Waste_Non-Hazardous_Incineration_Disamenity,3.01
Afghanistan,Non-Hazardous,Incineration,Waste Air pollution,/kg,Waste_Non-Hazardous_Incineration_Waste Air pollution,18.28
Afghanistan,Non-Hazardous,Incineration,Heavy metals and dioxins,/kg,Waste_Non-Hazardous_Incineration_Heavy metals and dioxins,4.93
Afghanistan,Hazardous,Unspecified,Leachate,/kg,Waste_Hazardous_Unspecified_Leachate,0.0
Afghanistan,Hazardous,Unspecified,Waste Air pollution,/kg,Waste_Hazardous_Unspecified_Waste Air pollution,18.28
Afghanistan,Hazardous,Unspecified,Heavy metals and dioxins,/kg,Waste_Hazardous_Unspecified_Heavy metals and dioxins,4.93
Afghanistan,Hazardous,Unspecified,Disamenity,/kg,Waste_Hazardous_Unspecified_Disamenity,3.01
Afghanistan,Hazardous,Unspecified,Waste GHGs,/kg,Waste_Hazardous_Unspecified_Waste GHGs,386.36
Afghanistan,Non-Hazardous,Unspecified,Leachate,/kg,Waste_Non-Hazardous_Unspecified_Leachate,0.3
Afghanistan,Non-Hazardous,Unspecified,Waste Air pollution,/kg,Waste_Non-Hazardous_Unspecified_Waste Air pollution,0.0
Afghanistan,Non-Hazardous,Unspecified,Heavy metals and dioxins,/kg,Waste_Non-Hazardous_Unspecified_Heavy metals and dioxins,0.0
Afghanistan,Non-Hazardous,Unspecified,Disamenity,/kg,Waste_Non-Hazardous_Unspecified_Disamenity,45.96
Afghanistan,Non-Hazardous,Unspecified,Waste GHGs,/kg,Waste_Non-Hazardous_Unspecified_Waste GHGs,179.15
```

### Water Consumption

```
Country,Category,Location,Impact,Units,Reference,Value
Afghanistan,N/A for WC,N/A for WC,Malnutrition,/m3,Water Consumption_N/A for WC_N/A for WC_Malnutrition,0.49
Afghanistan,N/A for WC,N/A for WC,Water-borne disease,/m3,Water Consumption_N/A for WC_N/A for WC_Water-borne disease,0.06
Afghanistan,N/A for WC,N/A for WC,Resource cost,/m3,Water Consumption_N/A for WC_N/A for WC_Resource cost,0.32
Afghanistan,N/A for WC,N/A for WC,Ecosystem services,/m3,Water Consumption_N/A for WC_N/A for WC_Ecosystem services,0.28
Albania,N/A for WC,N/A for WC,Malnutrition,/m3,Water Consumption_N/A for WC_N/A for WC_Malnutrition,0.02
Albania,N/A for WC,N/A for WC,Water-borne disease,/m3,Water Consumption_N/A for WC_N/A for WC_Water-borne disease,0.13
Albania,N/A for WC,N/A for WC,Resource cost,/m3,Water Consumption_N/A for WC_N/A for WC_Resource cost,1.0
Albania,N/A for WC,N/A for WC,Ecosystem services,/m3,Water Consumption_N/A for WC_N/A for WC_Ecosystem services,1.94
Algeria,N/A for WC,N/A for WC,Malnutrition,/m3,Water Consumption_N/A for WC_N/A for WC_Malnutrition,0.24
Algeria,N/A for WC,N/A for WC,Water-borne disease,/m3,Water Consumption_N/A for WC_N/A for WC_Water-borne disease,0.0
Algeria,N/A for WC,N/A for WC,Resource cost,/m3,Water Consumption_N/A for WC_N/A for WC_Resource cost,0.43
Algeria,N/A for WC,N/A for WC,Ecosystem services,/m3,Water Consumption_N/A for WC_N/A for WC_Ecosystem services,0.08
American Samoa,N/A for WC,N/A for WC,Malnutrition,/m3,Water Consumption_N/A for WC_N/A for WC_Malnutrition,0.3
American Samoa,N/A for WC,N/A for WC,Water-borne disease,/m3,Water Consumption_N/A for WC_N/A for WC_Water-borne disease,0.11
American Samoa,N/A for WC,N/A for WC,
```

# Water Pollution

```
Country,Category,Location,Impact,Units,Reference,Value
Afghanistan,Phosphorus,N/A for this Category,Eutrophication,/kg,Water Pollution_Phosphorus_N/A for this Category_Eutrophication,96.6218
Afghanistan,Nitrogen,N/A for this Category,Eutrophication,/kg,Water Pollution_Nitrogen_N/A for this Category_Eutrophication,0.0000
Afghanistan,Ag(I),Freshwater,Health,/kg,Water Pollution_Ag(I)_Freshwater_Health,41.6088
Afghanistan,Ag(I),Seawater,Health,/kg,Water Pollution_Ag(I)_Seawater_Health,0.8362
Afghanistan,Ag(I),Unspecified,Health,/kg,Water Pollution_Ag(I)_Unspecified_Health,41.6088
Afghanistan,As(III),Freshwater,Health,/kg,Water Pollution_As(III)_Freshwater_Health,"2,018.0068"
Afghanistan,As(III),Seawater,Health,/kg,Water Pollution_As(III)_Seawater_Health,169.1855
Afghanistan,As(III),Unspecified,Health,/kg,Water Pollution_As(III)_Unspecified_Health,"2,018.0068"
Afghanistan,As(V),Freshwater,Health,/kg,Water Pollution_As(V)_Freshwater_Health,"2,018.0068"
Afghanistan,As(V),Seawater,Health,/kg,Water Pollution_As(V)_Seawater_Health,169.1855
Afghanistan,As(V),Unspecified,Health,/kg,Water Pollution_As(V)_Unspecified_Health,"2,018.0068"
Afghanistan,Ba(II),Freshwater,Health,/kg,Water Pollution_Ba(II)_Freshwater_Health,64.0374
Afghanistan,Ba(II),Seawater,Health,/kg,Water Pollution_Ba(II)_Seawater_Health,12.9373
```

---

## Author (Source Database / GVFD)

- The International Foundation for Valuing Impacts (IFVI)

[![View Website](https://img.shields.io/badge/View-Website-blue)](https://www.ifvi.org)

## Author (Repository / Derivative Dataset)

- Daniel Rosehill  

[![View Website](https://img.shields.io/badge/View-Website-green)](https://danielrosehill.com)