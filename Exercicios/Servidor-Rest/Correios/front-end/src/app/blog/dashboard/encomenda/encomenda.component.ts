import { Encomendas } from './../../../shared/services/buscas/Encomendas';
import {Component} from "@angular/core";


@Component({
    selector: 'encomenda',
    templateUrl: 'encomenda.component',
    providers: [Encomendas]
})

export class EncomendaComponent {
    private servicePort:string = 'http://172.16.62.111:8091';
    private servicePath:string = '/your-application-ws/ws/';
    private targetNamespace:string = '';

    private responseJso:{} = null;

    private soapService:Encomendas;

    constructor() {
        this.soapService = new Encomendas(this.servicePort, this.servicePath, this.targetNamespace);
        this.soapService.envelopeBuilder = this.envelopeBuilder;
        this.soapService.jsoResponseHandler = (response:{}) => {this.responseJso = response};
        this.soapService.localNameMode = true;
    }

    private username:string = '';
    private password:string = '';

    public login(username:string, password:string) {
        var method:string = 'Login';
        var parameters:{}[] = [];

        this.username = username;
        this.password = password;

        parameters['LoginRequest xmlns="urn:application:security:messages:1:0"'] = UserAuthentication.userLogin(username, password);

        this.soapService.post(method, parameters);
    }

    private static userLogin(username, password):{}[] {
        var parameters:{}[] = [];

        parameters["UserName"] = username;
        parameters['Password'] = password;

        return parameters;
    }

    private envelopeBuilder(requestBody:string):string {
        return "<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\">" +
               "<SOAP-ENV:Header>" +
               "<wsse:Security SOAP-ENV:mustUnderstand=\"1\" xmlns:wsse=\"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd\" soapenv =\"http://schemas.xmlsoap.org/soap/envelope/\">" +
               "<wsse:UsernameToken wsu:ld=\"UsernameToken-104\" xmlns:wsu=\"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd\" >" +
                "<wsse:Username>" + this.username + "</wsse:Username>" +
                "<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText\">" + this.password + "</wsse:Password>" +
                "</wsse:UsernameToken>" +
                "</wsse:Security>" +
                "</SOAP-ENV:Header>" +
                "<SOAP-ENV:Body>" +
                requestBody +
                "</SOAP-ENV:Body>" +
                "</SOAP-ENV:Envelope>";
    }
}