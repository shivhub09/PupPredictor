import 'package:flutter/material.dart';

class GettingStarted extends StatelessWidget {
  const GettingStarted({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [Positioned(child: Image.asset('assets/GettingStarted.jpg'))],
      ),
    );
  }
}
