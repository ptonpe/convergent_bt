import { StyleSheet, Text, View, SafeAreaView, Pressable } from "react-native"
import React from 'react'
import { LinearGradient } from "expo-linear-gradient"
import { Entypo } from '@expo/vector-icons';
import { FontAwesome } from '@expo/vector-icons';

const LoginScreen = () => {
    const authenticate = () => {
        
    }
    return (
        <LinearGradient colors={["#040306", "#131624"]} style={{ flex: 1 }}>
            <SafeAreaView>
                <View style={{ height: 80 }} />
                <Entypo style={{ textAlign: "center" }} name="spotify" size={80} color="white" />
                <Text style={{
                    color: "white",
                    fontSize: 40,
                    fontWeight: "bold",
                    textAlign: "center",
                    marginTop: 40
                }}
                >
                    Spotify Recommender
                </Text>
                <View style={{ height: 80 }} />
                <Pressable
                onPress={authenticate}
                    style={{
                        backgroundColor: "#1DB954",
                        padding: 10, marginLeft: "auto",
                        marginRight: "auto",
                        width: 300,
                        borderRadius: 25,
                        alignItems: "center",
                        justifyContent: "center",
                        marginVertical:10
                    }}
                >
                    <Text>Sign in!</Text>
                </Pressable>

                <Pressable style={{
                    backgroundColor: "#131624", padding: 10, marginLeft: "auto",
                    marginRight: "auto",
                    width: 300,
                    borderRadius: 25,
                    alignItems: "center",
                    justifyContent: "center",
                    flexDirection:"row",
                    marginVertical:10,
                    borderColor:"#C0C0C0",
                    borderWidth:0.8
                }}>
                    <FontAwesome name="mobile-phone" size={24} color="white" />
                    <Text style={{fontWeight:"500",color:"white", textAlign:"center", flex:1}}> Use phone number</Text>

                </Pressable>
            </SafeAreaView>
        </LinearGradient>

    );
};

export default LoginScreen

const styles = StyleSheet.create({})