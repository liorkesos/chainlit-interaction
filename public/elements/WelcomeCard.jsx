import { MessageCircle } from "lucide-react";
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from "@/components/ui/card"; // Adjust the import path based on your setup

export default function WelcomeCard(props) {
    return (
        <Card className="w-full max-w-md mt-4">
            <CardHeader className="pb-2">
                <div className="flex justify-between items-center">
                    <CardTitle className="text-lg font-medium">
                        {props.title || 'Welcome'}
                    </CardTitle>
                </div>
                <CardDescription>{props.subtitle || 'AI Assistant'}</CardDescription>
            </CardHeader>
            <CardContent>
                <div className="flex items-center gap-2">
                    <MessageCircle className="h-4 w-4 opacity-70" />
                    <span className="text-sm">{props.message || 'How can I help you?'}</span>
                </div>
            </CardContent>
        </Card>
    );
}
