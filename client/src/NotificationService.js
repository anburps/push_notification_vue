import axios from "axios";
import { messaging, getToken } from "../firebase";

export async function requestNotificationPermission() {
    try {
        const permission = await Notification.requestPermission();
        if (permission === "granted") {
            const token = await getToken(messaging, {
                vapidKey: "YOUR_VAPID_KEY",
            });
            await axios.post("http://127.0.0.1:8000/api/register-token/", { token });
            console.log("Token registered:", token);
        } else {
            console.warn("Notification permission denied");
        }
    } catch (error) {
        console.error("Error getting notification permission:", error);
    }
}
