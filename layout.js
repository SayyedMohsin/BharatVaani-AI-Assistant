import React from "react";
import { Link, useLocation } from "react-router-dom";
import { createPageUrl } from "@/utils";
import { Mic, Home, Settings, CreditCard, MapPin, Globe } from "lucide-react";
import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarHeader,
  SidebarProvider,
  SidebarTrigger,
} from "@/components/ui/sidebar";

const navigationItems = [
  {
    title: "होम",
    titleEn: "Home",
    url: createPageUrl("Home"),
    icon: Home,
  },
  {
    title: "सेवाएं",
    titleEn: "Services", 
    url: createPageUrl("Services"),
    icon: CreditCard,
  },
  {
    title: "सेटिंग्स",
    titleEn: "Settings",
    url: createPageUrl("Settings"),
    icon: Settings,
  },
];

export default function Layout({ children, currentPageName }) {
  const location = useLocation();

  return (
    <div className="min-h-screen bg-gradient-to-br from-orange-50 via-white to-green-50">
      <style>
        {`
          @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap');
          
          :root {
            --saffron: #FF9933;
            --white: #FFFFFF;
            --green: #138808;
            --navy: #000080;
            --orange-50: #FFF7ED;
            --orange-100: #FFEDD5;
            --green-50: #F0FDF4;
          }
          
          .hindi-font {
            font-family: 'Noto Sans Devanagari', 'Inter', sans-serif;
          }
          
          .tricolor-gradient {
            background: linear-gradient(135deg, var(--saffron) 0%, var(--white) 50%, var(--green) 100%);
          }
        `}
      </style>
      
      <SidebarProvider>
        <div className="min-h-screen flex w-full">
          <Sidebar className="border-r border-orange-200 bg-white/80 backdrop-blur-sm">
            <SidebarHeader className="border-b border-orange-200 p-6">
              <div className="flex items-center gap-3">
                <div className="w-12 h-12 tricolor-gradient rounded-xl flex items-center justify-center shadow-lg">
                  <Mic className="w-6 h-6 text-white" />
                </div>
                <div className="hindi-font">
                  <h2 className="font-bold text-gray-900 text-lg">BharatVaani</h2>
                  <p className="text-sm text-gray-600">भारतीय भाषाओं का AI सहायक</p>
                </div>
              </div>
            </SidebarHeader>
            
            <SidebarContent className="p-3">
              <SidebarGroup>
                <SidebarGroupLabel className="text-xs font-semibold text-orange-700 uppercase tracking-wider px-3 py-2 hindi-font">
                  नेवीगेशन
                </SidebarGroupLabel>
                <SidebarGroupContent>
                  <SidebarMenu>
                    {navigationItems.map((item) => (
                      <SidebarMenuItem key={item.title}>
                        <SidebarMenuButton 
                          asChild 
                          className={`hover:bg-orange-50 hover:text-orange-700 transition-all duration-200 rounded-xl mb-1 hindi-font ${
                            location.pathname === item.url ? 'bg-orange-100 text-orange-800 shadow-sm' : 'text-gray-700'
                          }`}
                        >
                          <Link to={item.url} className="flex items-center gap-3 px-4 py-3">
                            <item.icon className="w-5 h-5" />
                            <span className="font-medium">{item.title}</span>
                          </Link>
                        </SidebarMenuButton>
                      </SidebarMenuItem>
                    ))}
                  </SidebarMenu>
                </SidebarGroupContent>
              </SidebarGroup>

              <SidebarGroup>
                <SidebarGroupLabel className="text-xs font-semibold text-green-700 uppercase tracking-wider px-3 py-2 hindi-font">
                  भाषाएं
                </SidebarGroupLabel>
                <SidebarGroupContent>
                  <div className="px-4 py-2 space-y-2">
                    <div className="flex items-center gap-2 text-sm hindi-font">
                      <Globe className="w-4 h-4 text-green-600" />
                      <span className="text-gray-700">समर्थित भाषाएं: 10+</span>
                    </div>
                    <div className="text-xs text-gray-500 hindi-font">
                      हिंदी • English • தமிழ் • తెలుగు • বাংলা • मराठी
                    </div>
                  </div>
                </SidebarGroupContent>
              </SidebarGroup>
            </SidebarContent>
          </Sidebar>

          <main className="flex-1 flex flex-col">
            <header className="bg-white/80 backdrop-blur-sm border-b border-orange-200 px-6 py-4 md:hidden">
              <div className="flex items-center gap-4">
                <SidebarTrigger className="hover:bg-orange-50 p-2 rounded-lg transition-colors duration-200" />
                <h1 className="text-xl font-bold hindi-font text-gray-900">BharatVaani</h1>
              </div>
            </header>

            <div className="flex-1 overflow-auto">
              {children}
            </div>
          </main>
        </div>
      </SidebarProvider>
    </div>
  );
}