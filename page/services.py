import React, { useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { CreditCard, Building2, MapPin, Heart, Umbrella, GraduationCap } from "lucide-react";
import { motion } from "framer-motion";
import { InvokeLLM } from "@/integrations/Core";

export default function ServicesPage() {
  const [searchQuery, setSearchQuery] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [searchResults, setSearchResults] = useState('');

  const handleServiceSearch = async (category, query) => {
    setIsLoading(true);
    setSearchResults('');

    try {
      const prompt = `
      भारतीय AI असिस्टेंट के रूप में ${category} के बारे में जानकारी दें:
      Query: ${query || 'सामान्य जानकारी'}
      
      कृपया विस्तार से हिंदी में जवाब दें और भारतीय संदर्भ में रखें।
      यदि यह सरकारी योजना है तो आवेदन प्रक्रिया भी बताएं।
      यदि यह स्थानीय सेवा है तो कैसे ढूंढें यह भी बताएं।
      `;

      const response = await InvokeLLM({
        prompt: prompt,
        add_context_from_internet: true
      });

      setSearchResults(response);
    } catch (error) {
      console.error('Error searching services:', error);
      setSearchResults('माफ करें, सेवा की जानकारी लेने में समस्या हुई है।');
    }

    setIsLoading(false);
  };

  const upiServices = [
    { name: "UPI बैलेंस चेक", desc: "अपना UPI बैलेंस देखें" },
    { name: "पेमेंट भेजना", desc: "किसी को पैसे भेजें" },
    { name: "QR कोड स्कैन", desc: "QR कोड से पेमेंट करें" },
    { name: "बिल पेमेंट", desc: "बिजली, पानी के बिल भरें" }
  ];

  const governmentSchemes = [
    { name: "आयुष्मान भारत", desc: "स्वास्थ्य बीमा योजना", icon: Heart },
    { name: "राशन कार्ड", desc: "खाद्य सुरक्षा योजना", icon: Building2 },
    { name: "PM किसान सम्मान निधि", desc: "किसानों के लिए आर्थिक सहायता", icon: Umbrella },
    { name: "बेटी बचाओ बेटी पढ़ाओ", desc: "बालिका कल्याण योजना", icon: GraduationCap }
  ];

  const localServices = [
    "डॉक्टर और अस्पताल",
    "प्लंबर और इलेक्ट्रीशियन", 
    "मिस्त्री और कारपेंटर",
    "ऑटो और टैक्सी सेवा",
    "किराना और दवाई की दुकान",
    "स्कूल और कॉलेज"
  ];

  return (
    <div className="min-h-screen p-4 md:p-8">
      <div className="max-w-6xl mx-auto space-y-8">
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center space-y-4"
        >
          <h1 className="text-3xl md:text-5xl font-bold bg-gradient-to-r from-blue-600 via-green-600 to-orange-600 bg-clip-text text-transparent hindi-font">
            सभी सेवाएं
          </h1>
          <p className="text-lg text-gray-700 hindi-font">
            UPI, सरकारी योजनाएं और स्थानीय सेवाएं - सब एक जगह
          </p>
        </motion.div>

        <Tabs defaultValue="upi" className="space-y-6">
          <TabsList className="grid w-full grid-cols-3 bg-white border-2 border-orange-200">
            <TabsTrigger value="upi" className="hindi-font font-medium">UPI सेवाएं</TabsTrigger>
            <TabsTrigger value="government" className="hindi-font font-medium">सरकारी योजनाएं</TabsTrigger>
            <TabsTrigger value="local" className="hindi-font font-medium">स्थानीय सेवाएं</TabsTrigger>
          </TabsList>

          {/* UPI Services */}
          <TabsContent value="upi" className="space-y-6">
            <Card className="border-2 border-blue-200 bg-blue-50/30">
              <CardHeader>
                <CardTitle className="flex items-center gap-3 hindi-font">
                  <CreditCard className="w-6 h-6 text-blue-600" />
                  UPI और डिजिटल पेमेंट
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid md:grid-cols-2 gap-4 mb-6">
                  {upiServices.map((service, index) => (
                    <Button
                      key={index}
                      onClick={() => handleServiceSearch('UPI सेवा', service.name)}
                      variant="outline"
                      className="justify-start h-auto p-4 border-blue-200 hover:bg-blue-50"
                    >
                      <div className="text-left">
                        <div className="font-semibold hindi-font">{service.name}</div>
                        <div className="text-sm text-gray-600 hindi-font">{service.desc}</div>
                      </div>
                    </Button>
                  ))}
                </div>
                
                <div className="space-y-3">
                  <Input
                    placeholder="UPI के बारे में कुछ और पूछें..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="hindi-font border-blue-200 focus:border-blue-400"
                  />
                  <Button
                    onClick={() => handleServiceSearch('UPI सेवा', searchQuery)}
                    disabled={isLoading}
                    className="w-full bg-blue-600 hover:bg-blue-700"
                  >
                    {isLoading ? 'खोज रहे हैं...' : 'खोजें'}
                  </Button>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Government Schemes */}
          <TabsContent value="government" className="space-y-6">
            <Card className="border-2 border-green-200 bg-green-50/30">
              <CardHeader>
                <CardTitle className="flex items-center gap-3 hindi-font">
                  <Building2 className="w-6 h-6 text-green-600" />
                  सरकारी योजनाएं
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid md:grid-cols-2 gap-4 mb-6">
                  {governmentSchemes.map((scheme, index) => (
                    <Button
                      key={index}
                      onClick={() => handleServiceSearch('सरकारी योजना', scheme.name)}
                      variant="outline"
                      className="justify-start h-auto p-4 border-green-200 hover:bg-green-50"
                    >
                      <scheme.icon className="w-8 h-8 text-green-600 mr-3" />
                      <div className="text-left">
                        <div className="font-semibold hindi-font">{scheme.name}</div>
                        <div className="text-sm text-gray-600 hindi-font">{scheme.desc}</div>
                      </div>
                    </Button>
                  ))}
                </div>
                
                <div className="space-y-3">
                  <Input
                    placeholder="सरकारी योजना के बारे में पूछें..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="hindi-font border-green-200 focus:border-green-400"
                  />
                  <Button
                    onClick={() => handleServiceSearch('सरकारी योजना', searchQuery)}
                    disabled={isLoading}
                    className="w-full bg-green-600 hover:bg-green-700"
                  >
                    {isLoading ? 'खोज रहे हैं...' : 'खोजें'}
                  </Button>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Local Services */}
          <TabsContent value="local" className="space-y-6">
            <Card className="border-2 border-orange-200 bg-orange-50/30">
              <CardHeader>
                <CardTitle className="flex items-center gap-3 hindi-font">
                  <MapPin className="w-6 h-6 text-orange-600" />
                  स्थानीय सेवाएं
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid md:grid-cols-2 gap-3 mb-6">
                  {localServices.map((service, index) => (
                    <Button
                      key={index}
                      onClick={() => handleServiceSearch('स्थानीय सेवा', service)}
                      variant="outline"
                      className="justify-start p-4 border-orange-200 hover:bg-orange-50 hindi-font font-medium"
                    >
                      {service}
                    </Button>
                  ))}
                </div>
                
                <div className="space-y-3">
                  <Input
                    placeholder="कोई स्थानीय सेवा ढूंढें..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="hindi-font border-orange-200 focus:border-orange-400"
                  />
                  <Button
                    onClick={() => handleServiceSearch('स्थानीय सेवा', searchQuery)}
                    disabled={isLoading}
                    className="w-full bg-orange-600 hover:bg-orange-700"
                  >
                    {isLoading ? 'खोज रहे हैं...' : 'खोजें'}
                  </Button>
                </div>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>

        {/* Search Results */}
        {searchResults && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
          >
            <Card className="border-2 border-purple-200 bg-purple-50/30">
              <CardHeader>
                <CardTitle className="hindi-font text-purple-800">
                  खोज के परिणाम
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="prose max-w-none hindi-font">
                  <p className="text-gray-800 leading-relaxed whitespace-pre-wrap">
                    {searchResults}
                  </p>
                </div>
              </CardContent>
            </Card>
          </motion.div>
        )}
      </div>
    </div>
  );
}