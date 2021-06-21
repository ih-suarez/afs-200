//
//  AppApp.swift
//  Shared
//
//  Created by Ismael Suarez on 6/20/21.
//

import SwiftUI

@main
struct AppApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: AppDocument()) { file in
            ContentView(document: file.$document)
        }
    }
}
